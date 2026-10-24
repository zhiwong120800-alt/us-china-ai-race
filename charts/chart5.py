import pandas as pd
import plotly.express as px
import streamlit as st

# Load the data
file_path = "data/raw/epoch_notable_ai_models_20261020.csv" 
df = pd.read_csv(file_path)

# Tag Countries
# Epoch usually uses "United States" and "China"
def tag_country(row):
    countries = str(row['Country (of organization)'])
    if 'United States' in countries:
        return 'US'
    elif 'China' in countries:
        return 'CN'
    elif 'Multinational' in countries:
        return 'Multinational'
    else:
        return 'Other'

df['Country_Tag'] = df.apply(tag_country, axis=1)
# Keep only US and CN for this chart
df = df[df['Country_Tag'].isin(['US', 'CN'])]

# Tag Periods
df['Year'] = pd.to_datetime(df['Publication date']).dt.year
def get_period(year):
    if 2016 <= year <= 2019: return '2016–2019'
    elif 2020 <= year <= 2022: return '2020–2022'
    elif 2023 <= year <= 2025: return '2023–2025'
    else: return None
df['Period'] = df['Year'].apply(get_period)
df = df.dropna(subset=['Period'])

# Group Model Accessibility 
def group_accessibility(val):
    val = str(val).lower()
    if 'open weights' in val:
        return 'Open weights'
    elif 'api' in val or 'hosted' in val:
        return 'API / hosted'
    elif 'unreleased' in val:
        return 'Unreleased'
    else:
        return 'Unknown'

df['Access_Group'] = df['Model accessibility'].apply(group_accessibility)

# Calculate percentages
# Group by Country, Period, and Access_Group
counts = df.groupby(['Country_Tag', 'Period', 'Access_Group']).size().reset_index(name='Count')
# Calculate total models per country/period to get the base for 100%
totals = counts.groupby(['Country_Tag', 'Period'])['Count'].transform('sum')
counts['Percentage'] = (counts['Count'] / totals) * 100

# Sort the rows so US is on top, then China, and periods are chronological
counts['Row_Label'] = counts['Country_Tag'] + ' ' + counts['Period']
row_order = ['US 2016–2019', 'US 2020–2022', 'US 2023–2025', 
             'CN 2016–2019', 'CN 2020–2022', 'CN 2023–2025']

# Build the Chart
fig = px.bar(
    counts, 
    x='Percentage', 
    y='Row_Label', 
    color='Access_Group',
    orientation='h',
    text='Percentage', # Puts numbers on the chart
    category_orders={"Row_Label": row_order, "Access_Group": ['Open weights', 'API / hosted', 'Unreleased', 'Unknown']},
    title="Chart 5: Open vs Closed (US vs China)"
)

# Format text to show 1 decimal place
fig.update_traces(texttemplate='%{text:.1f}%', textposition='inside')

# Update layout to make it a 100% stacked bar
fig.update_layout(
    barmode='stack',
    xaxis_title="Percentage of Models",
    yaxis_title="Country and Period",
    xaxis=dict(range=[0, 100]) # Force x-axis to 0-100
)

st.plotly_chart(fig, use_container_width=True)