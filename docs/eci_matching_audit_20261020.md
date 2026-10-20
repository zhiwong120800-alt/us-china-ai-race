# ECI × Epoch Notable Models: Chart 6 coverage audit

**Frozen working files:** ECI model scores downloaded 2026-10-20 (website updated 2026-10-19); Epoch Notable AI Models frozen 2026-10-20. Exact source bytes stored in `data/raw/`. **Version caution:** ECI model release dates include through 2026-10-07, while the latest publication date in the Notable snapshot is 2026-09-30.

## Summary

- ECI model scores: **277** distinct named models, release years 2023–2026. Notable Models: **1078** distinct model names, publication years 1950–2026.
- Exact (case-sensitive) `Model` name matches: **111/277 = 40.1%**; unmatched **166**. Matching is not model-family matching, and it is not fuzzy. An unmatched ECI model is **not** proof that it lacks a corresponding model family in Notable Models.
- ECI country missing: **17** records. These are not assigned to US or China.
- Date discrepancies among exact matches: **22**, including **3** with differing calendar years. Use **ECI `date`** consistently for Chart 6 capability trend; do not silently use the Notable publication date for that trend.
- `model_versions` field in uploaded ECI is entirely blank. It cannot serve as a join key.

## US–China country coverage (ECI denominator)

| Group | ECI entries | Matched exactly | Exact-match % of ECI | Of matched, known training FLOP | FLOP % of matched |
|---|---:|---:|---:|---:|---:|
| United States | 161 | 78 | 48.4% | 23 | 29.5% |
| China | 76 | 29 | 38.2% | 21 | 72.4% |
| **Total US + China** | 237 | 107 | 45.1% | 44 | 41.1% |

The overall ECI **111** matches include other countries; do not confuse this with the US + China **107** matched records.

## Audit by release year

| Country | ECI year | ECI entries | Exact matches | Match % of ECI | FLOP usable | Same-year Notable count† |
|---|---:|---:|---:|---:|---:|---:|
| US | 2023 | 23 | 8 | 34.8% | 6 | 86 |
| US | 2024 | 44 | 15 | 34.1% | 5 | 57 |
| US | 2025 | 46 | 28 | 60.9% | 9 | 64 |
| US | 2026 | 48 | 27 | 56.2% | 3 | 49 |
| China | 2023 | 11 | 1 | 9.1% | 1 | 23 |
| China | 2024 | 9 | 4 | 44.4% | 4 | 31 |
| China | 2025 | 23 | 9 | 39.1% | 9 | 35 |
| China | 2026 | 33 | 15 | 45.5% | 7 | 29 |

† This is a contextual same-calendar-year Notable count, **not** a clean country-level match-rate denominator: dates can differ between sources, and source scopes differ. Use ECI as the denominator for the exact-match coverage table. Individual model cross-dataset identification is performed only on exact model names.

## Implications for Chart 6

1. **Capability trend (line)**: Use `chart6_eci_us_china_full_country_scores.csv`, which uses ECI's own country field and retains all **US 161 + China 76** ECI records. No need to join to Notable to compare available ECI scores. Report that this is a selected benchmark-evaluated language-model dataset, not a national capability census. Construct a stepwise best-to-date frontier by release date (do not treat missing monthly releases as zero; show source date).
2. **Compute vs capability (scatter)**: Use **44** conservatively exact-matched US/China models with valid Epoch Notable training compute from `chart6_compute_scatter_us_china_exact.csv` (**US 23, China 21**). The cross-country coverage imbalance and year mix are substantial. Do not assert a population-level model efficiency comparison from this selected sample.
3. **Unmatched review**: `chart6_eci_unmatched_review.csv` provides human-review *suggestions*, **not approved joins**. Model names can refer to preview, dated, tuned or serving variants. Approve matches only after checking official model identifiers, release variants, and source links; log decisions and test them.
4. **Discrepant release dates**: `chart6_eci_date_discrepancies.csv` lists all exact-name cases with different dates. Changing date source can shift a model into another month or year. The user-visible chart should state which date column is used.
5. **Confidence intervals**: ECI includes `eci_ci_low` and `eci_ci_high`; 2 models lack intervals. Consider them for uncertainty display rather than treating decimal ECI scores as error-free.
6. **Chart 1–5 versus Chart 6**: Notable Models covers a broader, intentionally selected research sample; ECI focuses on benchmark-evaluated models, predominantly recent LLMs. Do not claim the Chart 6 subset represents the entire Chart 1–5 model population.

## Reproduce

From the project root, run `python scripts/build_eci_audit.py`. It reads only the two frozen raw CSVs. The script uses Python standard library `csv`, does exact model-name joins, checks duplicate keys and country agreement, and writes five auditable processed tables plus the human-review list. No values were manually inserted into the generated CSVs.

## Data dictionary for these outputs

- Raw ECI source: [Epoch Capabilities Index](https://epoch.ai/eci), 2026-10-19 data update shown on download page, working copy downloaded 2026-10-20; CC BY 4.0 per published download information (verify exact terms when publishing). Unit `eci`: ECI index points. `eci_ci_low`/`eci_ci_high`: lower/upper interval in ECI points. `date`: ECI model release date, YYYY-MM-DD. `Model`: text key, unique in this file. `Country (of organization)`: source-assigned organisation country. Last model release observation: **2026-10-07**.
- Raw Notable source: [Epoch AI Models](https://epoch.ai/data/ai-models), working copy downloaded 2026-10-20; check official dataset licence at publication. Unique key for this frozen file: `Model`. `Training compute (FLOP)`: floating-point operations; some estimates and missing values. `Publication date`: date published in Epoch Notable snapshot, YYYY-MM-DD; latest 2026-09-30.
- `chart6_eci_notable_exact_join.csv`: primary key `Model`, one row per ECI model; exact join only. `exact_name_match`, `compute_available`: 0/1; `eci_year`: YYYY.
- `chart6_eci_us_china_full_country_scores.csv`: primary key `(Model,country)`; only US and China with ECI country assignment; dates, ECI estimates and interval in ECI units; country-specific selection from ECI raw.
- `chart6_compute_scatter_us_china_exact.csv`: primary key `(Model,country)`; conservative matched sample; x = `training_compute_flop` in FLOP, y = `eci` in ECI points; date defined by ECI; data sourced from exact-name cross-dataset join.
- `chart6_eci_country_year_coverage.csv`: primary key `(country,eci_year)`; counts of models; match percentages use ECI models in same country and release year; `%` units; same-year Notable counts are descriptive only.
- `chart6_eci_date_discrepancies.csv`: primary key `Model`; contains ECI and Notable dates where inconsistent.
- `chart6_eci_unmatched_review.csv`: primary key `ECI_Model`; suggestions are advisory only, not joins.
