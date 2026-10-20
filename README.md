# US–China AI Race: Beyond the Numbers

**UTS · 36104 Data Visualisation and Narratives · Assignment 3**

> **Research question:** Does the US–China AI race look the same when we count papers, count models, and test model performance?

**Persona:** A foreign policy analyst who wants to identify which dimensions of competition genuinely differ and which metrics can mislead.

**Status (2026-10-20): initial shared-data snapshot only.** The full Streamlit application and individual charts are still being developed. The processed files are analysis inputs and audits, *not* final narrative conclusions.

## Three user stories (planned final app)

1. As a foreign policy analyst, I want to compare papers and model counts side by side, so that I can see whether research output indicates model development.
2. As a foreign policy analyst, I want to filter release strategy by developer type, so that I can examine whether openness varies more by organisations or by country.
3. As a foreign policy analyst, I want to compare compute and ECI benchmark scores, so that I can understand how much training inputs align with measured capabilities.

## Charts and owners

| Chart | Focus | Owner | Status |
|---|---|---|---|
| 1 | Papers vs Models | Wang | Processed data ready, chart pending |
| 2 | Frontier Gap | Aditi | Raw Epoch data ready, chart pending |
| 3 | Who Builds It | Manasvi | Raw Epoch data ready, chart pending |
| 4 | Industry vs Academia | Wang | Raw Epoch data ready; taxonomy review pending |
| 5 | Open vs Closed | Maris | Raw Epoch data ready; access taxonomy review pending |
| 6 | Volume vs Quality | Wang | ECI coverage audit ready, charts pending; paper citation source under review |

## Files to use

| If you work on... | Begin with... |
|---|---|
| Chart 1 | `data/processed/chart1_papers_vs_models_2016_2024.csv` |
| Charts 2–5 | `data/raw/epoch_notable_ai_models_20261020.csv` |
| Chart 6 (ECI trend) | `data/processed/chart6_eci_us_china_full_country_scores.csv` |
| Chart 6 (compute × capability) | `data/processed/chart6_compute_scatter_us_china_exact.csv` |
| ECI match checks | `docs/eci_matching_audit_20261020.md` |

See **[Data dictionary](docs/data_dictionary.md)** for columns, units, keys and time coverage, and **[data sources and licences](docs/data_sources_and_licenses.md)** for exact citations and reuse conditions.

## Reproduce frozen-data processing

Prerequisite: Python 3.10+ (scripts use the standard library; no extra packages needed at this stage).

```bash
python scripts/build_chart1.py
python scripts/build_eci_audit.py
```

The scripts read unmodified source files under `data/raw/` and regenerate the relevant CSVs under `data/processed/`. Do not silently edit those source files. Check `docs/source_checksums.sha256` before changing any snapshot.

## Interpretation caveats

- A **notable model** in Epoch is a selectively curated entry, not every AI model made in a country.
- Country labels are based on developing organisations; where both US and China appear, whole counting assigns the model to both.
- Paper counts only cover works with English titles or abstracts; cross-country collaborative papers count in each country.
- Training FLOPs measure resource inputs, not performance.
- ECI evaluations cover a different and narrower model population. Scatter-plot eligibility is substantially smaller after linking ECI to Notable and requiring a compute estimate. Do **not** describe it as representing all models.
- The 2026-10-20 files are a **fixed snapshot**; newer downloads will produce different statistics. Displays should distinguish observation dates from snapshot dates.

## Data & AI provenance

- Dataset lineage, licence notes and attribution: `docs/data_sources_and_licenses.md`.
- ECI linkage and review records: `docs/eci_matching_audit_20261020.md`, `data/processed/chart6_eci_unmatched_review.csv`.
- AI usage: `docs/ai_provenance_template.csv`; each group member supplies an accurate row with a verification that *could have failed*.
- Draft statement for group review: `docs/data_ai_disclosure_draft.md`.

## Development / assessment

Part 1 recording: **2026-10-23** (per group guide). Part 2: **2026-11-20**. The final submission must identify the deployed app URL, the repository URL and a final commit hash/tag. This initial package is not a complete Part 2 submission.

**Source licences are not the same as a licence for our code.** The repository does not declare a blanket open-source licence: Epoch material requires attribution, and the CSET dataset redistributed by OWID is **CC BY-NC 4.0**. Refer to the original publishers' terms.
