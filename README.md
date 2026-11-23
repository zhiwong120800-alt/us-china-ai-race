# The AI Race: Beyond the Numbers

**UTS 36104 — Data Visualisation & Narratives — Assignment 3 Part 2**

**Research question:** Does the US–China AI race look the same when we count research papers, count notable models, and test model performance?

**Persona / decision served:** A foreign policy analyst deciding which cross-country comparisons are informative and which are misleading because populations, denominators, definitions or measurements differ.

**Answer:** No single scoreboard settles the comparison. China leads the 2024 paper count in the selected source, while the US leads Epoch's 2024 notable-model count; industry participation is similar under a narrow definition, release patterns differ, and the selected benchmark and compute samples give other perspectives. This is not a national AI capability ranking.

## Run the assessed six-chapter application

Python 3.11+ recommended:

    python -m pip install -r requirements.txt
    streamlit run app.py

The app is **Streamlit** (not just a GitHub Pages preview). The eight trusted HTML/JS pages under static/ are shipped **in the same commit** and embedded using Streamlit's st.iframe. Use the sidebar or the Previous/Next chapter navigation. Static-file serving is configured in .streamlit/config.toml.

GitHub Pages [read-only preview](https://zhiwong120800-alt.github.io/us-china-ai-race/) contains the same frozen study narrative but is not a substitute for the assessed Streamlit Cloud deployment. A public Streamlit Cloud URL must be created and verified before the final submission PDF is issued; it is **not** assumed to exist.

## Three demonstrable user stories

1. **As a foreign policy analyst, I want** to compare 2016–2024 AI publication counts with notable-model counts, **so that** I can see why research output and model development provide different rankings. **Path:** Introduction → Chapter 01; change years and counts/share mode.
2. **As a foreign policy analyst, I want** to filter model release strategy by developer type and country, **so that** I can distinguish the national release mix from the industry/academic mix. **Path:** Chapter 05; change period, developer type and share/count; inspect model records.
3. **As a foreign policy analyst, I want** to compare dated training compute with model-level ECI performance, **so that** I can judge which capability claims are and are not supported. **Path:** Chapters 02 and 06; change period and country, inspect models and the 44-record compute match.

## Six analytical chapters

| Chapter | Question | Main evidence |
|---|---|---|
| 01 Papers vs Models | Does publication volume predict notable-model count? | CSET via OWID and Epoch, 2016–2024 |
| 02 Frontier Gap | How does reported peak training compute evolve? | Epoch Notable Models, 2016–Sep 2026 |
| 03 Who Builds It? | How concentrated is developer participation? | Audited source organisations, 2016–2025; optional Hong Kong sensitivity |
| 04 Industry vs Academia | How sensitive are industry shares to collaboration? | 667 model–country observations, 2016–2025 |
| 05 Open vs Closed | Does access differ by developer type? | Same 667 reviewed model–country observations |
| 06 Volume vs Quality | Does a model count or compute estimate establish capability? | 237 ECI model–country observations, including 44 exact name/compute matches |
| Conclusion | Do all six perspectives agree? | Integrative answer with study limits and cross-referenced literature |

## Team Contributions

The project combines individually developed analysis with subsequent integration, data validation and quality assurance. The following distinguishes original chapter work from project-wide integration.

| Member | Documented contribution |
|---|---|
| **Zhi Wang — Project Integration Lead** | Integrated the six-chapter narrative into the Streamlit application; implemented and debugged navigation and interactions; reconciled cross-chapter counting and model-level classifications; prepared data-validation and reproducibility scripts, automated acceptance checks, repository documentation and final rubric audit. |
| **Aditi** | Chapter 02 — Frontier Gap: original analysis and visualisation of AI training-compute trends. |
| **Manasvi** | Chapter 03 — Who Builds It?: original developer-concentration analysis, organisation groupings and country attribution review. |
| **Maris** | Chart 05 — Open vs Closed: original Streamlit/Plotly release-strategy visualisation. |

All chapters underwent further integration and review. GitHub commits, the data-review inputs and reconstruction scripts document the integration process; a single account's commit history does not independently establish authorship of every original contribution.

## Data and reconstruction

**Frozen download / processing date: 20 October 2026.** OWID paper latest observation: **2024** (upstream metadata updated 27 April 2026). Epoch Notable latest model publication date: **30 September 2026**. ECI latest model release date: **7 October 2026**.

- data/raw/ — immutable Epoch and CSET/OWID source snapshots.
- data/review/ — *human-reviewed inputs* recovered from the team's published Chapter 3–5 model-level records, including explicit mapping decisions. They are **not** independently sourced raw data.
- data/processed/ — calculated outputs for all chapters, including 667 matched model–country assignments and the original ECI matching audit.
- docs/data_dictionary.md — every CSV, source, licence, fields, units, keys, time coverage and transformation.
- docs/data_sources_and_licenses.md — source attribution and reuse restrictions.
- docs/eci_matching_audit_20261020.md — exact-name matching and date discrepancies.
- docs/REPRODUCIBILITY.md — verification instructions and caveats.

From the repository root:

    python scripts/build_chart1.py
    python scripts/build_chart2.py
    python scripts/build_eci_audit.py
    python scripts/rebuild_chapter_data.py

The CI workflow .github/workflows/portfolio-checks.yml runs source-to-output checks and tests that the Streamlit app serves all eight bundled pages. Consult its status before submission.

**Counting and attribution:** a jointly developed US–China model can appear once in each country's records. Rankings use participation, not exclusive model ownership. Chapter 3's optional Hong Kong mode is not part of the default 667-record US/China denominator. Open weights is not synonymous with complete open-source access. Published training FLOPs measure inputs, not model quality. ECI is a selected evaluation suite, not a national census.

## Data and AI use

See docs/ai_provenance_matrix.csv and docs/data_ai_disclosure.md. A complete AI-use record must be provided by *every* group member, each with a verification that could have failed. **Four members are listed. Aditi and Manasvi have confirmed their chapter contributions and authorised delegated maintenance of the matrix; their individual AI tool/prompt/output and verification details are not yet documented. These rows must not be treated as verified AI-use records until those particulars are established.**

## Final Part 2 delivery

Submit **one PDF** containing (1) the **live Streamlit deployment URL**, (2) this GitHub repository URL, and (3) the immutable **main commit SHA** for the version being graded. The team must verify the Streamlit app responds at 1366 × 768, all user stories work, and the AI provenance matrix and disclosure are final. The complete submission instructions are in docs/FINAL_SUBMISSION_CHECKLIST.md.

This repository is coursework; its source licences are not blanket licences for code or data. CSET input used through OWID carries **CC BY-NC 4.0**; see the source register.
