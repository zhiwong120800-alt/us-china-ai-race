"""UTS 36104 — The AI Race. Frozen 2026-10-20 data narrative edition."""
from pathlib import Path
import json
import streamlit as st

st.set_page_config(page_title="The AI Race — United States and China", layout="wide", initial_sidebar_state="expanded")
PAGES = [
    [
        "Introduction",
        "index.html"
    ],
    [
        "01 · Papers vs Models",
        "Chapter_01_Papers_vs_Models.html"
    ],
    [
        "02 · Frontier Gap",
        "Chapter_02_Frontier_Gap.html"
    ],
    [
        "03 · Who Builds It?",
        "Chapter_03_Who_Builds_It_Integrated.html"
    ],
    [
        "04 · Industry vs Academia",
        "Chapter_04_Industry_Academia.html"
    ],
    [
        "05 · Open vs Closed",
        "Chapter_05_Open_vs_Closed.html"
    ],
    [
        "06 · Volume vs Quality",
        "Chapter_06_Volume_vs_Quality.html"
    ],
    [
        "Conclusion",
        "Conclusion.html"
    ]
]
LABELS = [label for label, _ in PAGES]
ROOT = Path(__file__).resolve().parent
requested = st.query_params.get("page", "Introduction")
if requested not in LABELS:
    requested = LABELS[0]
if "chapter_selection" not in st.session_state:
    st.session_state.chapter_selection = requested

def go_to_chapter(target_index: int) -> None:
    """Button callback: runs before st.radio(key='chapter_selection') is instantiated."""
    target = LABELS[target_index]
    st.session_state["chapter_selection"] = target
    st.query_params["page"] = target
    st.session_state["_chapter_scroll_pending"] = True

# The static pages run in a same-origin iframe. Streamlit sandboxes top-level
# iframe navigation, so their chapter links post an explicit, allowlisted
# message to this trusted host rather than attempting to navigate the iframe.
# The host performs a same-tab navigation, synchronising the sidebar + URL.
_NAV_MAP = {filename: label for label, filename in PAGES}
_NAV_SCRIPT = """
<script>
(() => {
  const destinations = __PAGE_MAP__;
  if (window.__aiRaceHostNavigation) {
    window.removeEventListener("message", window.__aiRaceHostNavigation);
  }
  window.__aiRaceHostNavigation = (event) => {
    if (event.origin !== window.location.origin) return;
    if (event.data?.type !== "ai-race:chapter-navigation") return;
    const label = destinations[event.data.file];
    if (!label) return;
    const destination = new URL(window.location.href);
    if (destination.searchParams.get("page") === label) {
      window.scrollTo({top: 0, behavior: "instant"});
      return;
    }
    destination.searchParams.set("page", label);
    destination.hash = "";
    window.location.assign(destination.href);
  };
  window.addEventListener("message", window.__aiRaceHostNavigation);
})();
</script>
""".replace("__PAGE_MAP__", json.dumps(_NAV_MAP, ensure_ascii=False))
st.html(_NAV_SCRIPT, unsafe_allow_javascript=True)

with st.sidebar:
    st.markdown("### THE AI RACE")
    selection = st.radio("Explore the evidence", LABELS, key="chapter_selection")
    if st.query_params.get("page") != selection:
        st.query_params["page"] = selection
    st.caption("UTS 36104 · Interactive data narrative")
    st.caption("Frozen sources: 20 October 2026 · CSET/OWID and Epoch AI")
    st.markdown("[Data dictionary and limitations](https://github.com/zhiwong120800-alt/us-china-ai-race/blob/main/docs/data_dictionary.md)")

idx = LABELS.index(selection)
# Streamlit's main content is a scrollable section, not necessarily window.
# Trigger this only after a native Next/Previous callback changes chapter.
if st.session_state.pop("_chapter_scroll_pending", False):
    st.html(
        """
        <script>
        (() => {
          const toTop = () => {
            const candidates = [
              document.scrollingElement,
              document.querySelector('[data-testid="stMain"]'),
              document.querySelector('.stMain'),
              document.querySelector('[data-testid="stAppViewContainer"]'),
              document.querySelector('section.main'),
              document.querySelector('[data-testid="stMainBlockContainer"]')
            ];
            for (const el of candidates) {
              if (el) el.scrollTop = 0;
            }
            window.scrollTo(0, 0);
          };
          toTop();
          requestAnimationFrame(() => requestAnimationFrame(toTop));
          setTimeout(toTop, 120);
        })();
        </script>
        """,
        unsafe_allow_javascript=True,
    )

if idx == 0:
    st.markdown("**Research question:** Does the US–China AI race look the same when we count papers, count notable models and test model performance?")
source = ROOT / "static" / PAGES[idx][1]
if not source.is_file():
    st.error(f"The page {source.name} is missing from this commit.")
    st.stop()
# Trusted, version-controlled local HTML keeps the six existing interactive
# visuals and JavaScript without linking to a mutable GitHub Pages version.
# Auto-size the iframe to its content rather than using a fixed scrolling pane.
st.iframe(source, height="content", alt=f"The AI Race: {selection}")
# Expose the assessed data independently of hover-only chart interactions.
# The table is lazy to keep the normal page load fast.
DATA_TABLES = {
    0: "data/processed/chart1_papers_vs_models_2016_2024.csv",
    1: "data/processed/chart1_papers_vs_models_2016_2024.csv",
    2: "data/raw/epoch_notable_ai_models_20261020.csv",
    3: "data/processed/chart3_affiliations.csv",
    4: "data/processed/chart4_model_type_records.csv",
    5: "data/processed/chart5_model_access_records.csv",
    6: "data/processed/chart6_eci_us_china_full_country_scores.csv",
    7: "data/processed/chart6_eci_us_china_full_country_scores.csv",
}
if st.toggle("Show exact data table (no hovering required)", value=False, key="show_source_table"):
    import pandas as pd
    source_csv = ROOT / DATA_TABLES[idx]
    if source_csv.is_file():
        @st.cache_data(show_spinner=False)
        def read_source(path: str):
            return pd.read_csv(path, low_memory=False)
        table = read_source(str(source_csv))
        st.caption(f"Frozen source table: {source_csv.relative_to(ROOT)} · {len(table):,} rows")
        st.dataframe(table, use_container_width=True, hide_index=True, height=330)
    else:
        st.warning(f"Missing reproducible table: {source_csv.name}")

left, center, right = st.columns([1, 2, 1])
with left:
    if idx:
        st.button(
            "← Previous", use_container_width=True,
            on_click=go_to_chapter, args=(idx - 1,),
        )
with center:
    st.caption("Version-controlled interactive chapters · Original source data and review rules available in this repository.")
with right:
    if idx < len(PAGES) - 1:
        st.button(
            "Next →", use_container_width=True,
            on_click=go_to_chapter, args=(idx + 1,),
        )
