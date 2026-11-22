"""Legacy standalone Chart 5 view using the same reviewed 667 records as the final site.

Main Streamlit entry point is app.py (all six chapters). This module is kept as
a reproducible native Streamlit alternative for the release-strategy plot.
"""
import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data(show_spinner=False)
def load_data():
    return pd.read_csv("data/processed/chart5_model_access_records.csv")

def render_chart5():
    st.header("Release strategies — US and China")
    st.caption("Source: Epoch AI notable models, 20 Oct 2026 frozen snapshot; multi-country models credited once per country.")
    df=load_data().copy()
    df["Country"]=df["country"].map({"US":"United States","China":"China"})
    periods=["2016–2019","2020–2022","2023–2025"]
    types=["Industry","Academia","Collaboration","Other","Unknown"]
    countries=st.multiselect("Country",["United States","China"],default=["United States","China"])
    selected_periods=st.multiselect("Period",periods,default=["2023–2025"])
    selected_types=st.multiselect("Developer type",types,default=types)
    selected=df[df.Country.isin(countries)&df.period.isin(selected_periods)&df.developer_type.isin(selected_types)]
    if selected.empty:
        st.info("No matching model records. Widen the period, country or developer-type filter.")
        return
    counts=selected.groupby(["Country","period","release_strategy"]).size().reset_index(name="count")
    counts["total"]=counts.groupby(["Country","period"])["count"].transform("sum")
    counts["percentage"]=100*counts["count"]/counts["total"]
    counts["label"]=counts["Country"]+" · "+counts["period"]
    strategy_order=["Open weights","API / hosted","Unreleased","Unknown"]
    fig=px.bar(counts,x="percentage",y="label",color="release_strategy",orientation="h",
        category_orders={"release_strategy":strategy_order},
        color_discrete_map={"Open weights":"#126b53","API / hosted":"#92b6b0","Unreleased":"#e5cb9c","Unknown":"#deddd7"},
        labels={"percentage":"Share of selected model–country records (%)","label":"Country and period","release_strategy":"Access category"},
        title="How notable models were released, by country and period")
    fig.update_layout(barmode="stack",xaxis=dict(range=[0,100]),legend_title_text="Release category")
    st.plotly_chart(fig,use_container_width=True)
    st.caption("The denominator changes when developer types are filtered. Open weights does not mean fully open source.")
    with st.expander("Read exact values without hovering"):
        st.dataframe(counts[["Country","period","release_strategy","count","total","percentage"]],hide_index=True,use_container_width=True)
    with st.expander("Limitations"):
        st.write("Curated notable models, not a census. Whole-counted multinational collaborations. Access categories are distinct from model capability, training transparency and safety.")
