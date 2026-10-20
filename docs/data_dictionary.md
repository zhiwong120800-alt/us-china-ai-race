# Data dictionary — working version (20 Oct 2026)

This dictionary lists **every CSV presently included in the repository**. Raw files are snapshots and are not modified; processed files are regenerated from documented scripts. Inferred units and semantic definitions should be checked against the [Epoch field documentation](https://epoch.ai/data/ai-models-documentation) before final Part 2 submission.

Definitions: **Primary key** can be a *composite key*; observation coverage refers to model/publication dates, not download dates. `Model` is unique in this snapshot, not a permanent identifier across future versions.

## `data/processed/chart1_papers_vs_models_2016_2024.csv`

- **Source / provider:** CSET/OWID + Epoch Notable — [source register](data_sources_and_licenses.md)
- **File role:** Derived output
- **Primary key in frozen file:** `year + country` (check uniqueness in future updates)
- **Rows / columns:** 18 / 7
- **Observation range / latest:** year: 2016 to 2024
- **Source licence:** Inherited from underlying source(s), see source register
- **Transform:** Whole-country model counting; join to paper counts by country/year; compute two-country shares

| Column | Units or meaning |
|---|---|
| `year` | calendar year |
| `country` | US or China label |
| `country_code` | ISO3 |
| `ai_publications` | publications/year |
| `epoch_notable_models` | models/year |
| `share_of_two_country_publications_pct` | percent (%) |
| `share_of_two_country_models_pct` | percent (%) |

## `data/processed/chart6_compute_scatter_us_china_exact.csv`

- **Source / provider:** Epoch ECI + Notable — [source register](data_sources_and_licenses.md)
- **File role:** Derived output
- **Primary key in frozen file:** `Model + country` (check uniqueness in future updates)
- **Rows / columns:** 44 / 10
- **Observation range / latest:** eci_year: 2023 to 2026; eci_release_date: 2023-02-24 to 2026-09-09
- **Source licence:** Inherited from underlying source(s), see source register
- **Transform:** Restrict to matched US/China ECI models with known training compute

| Column | Units or meaning |
|---|---|
| `Model` | model name / record ID |
| `country` | US or China label |
| `eci_release_date` | date YYYY-MM-DD |
| `eci_year` | calendar year |
| `eci` | ECI score (index units) |
| `eci_ci_low` | ECI score, lower confidence bound |
| `eci_ci_high` | ECI score, upper confidence bound |
| `training_compute_flop` | FLOP |
| `notable_publication_date` | date YYYY-MM-DD |
| `notable_domain` | category |

## `data/processed/chart6_eci_country_year_coverage.csv`

- **Source / provider:** Epoch ECI + Notable — [source register](data_sources_and_licenses.md)
- **File role:** Derived output
- **Primary key in frozen file:** `country + eci_year` (check uniqueness in future updates)
- **Rows / columns:** 8 / 10
- **Observation range / latest:** eci_year: 2023 to 2026
- **Source licence:** Inherited from underlying source(s), see source register
- **Transform:** Year-country eligibility and compute matching audit

| Column | Units or meaning |
|---|---|
| `country` | US or China label |
| `eci_year` | calendar year |
| `eci_models` | models |
| `exact_matched_eci_models` | models |
| `match_pct_of_eci` | percent (%) |
| `matched_with_training_compute` | models |
| `compute_pct_of_matched` | percent (%) |
| `notable_models_same_calendar_year` | models |
| `matched_div_notable_same_year_pct_DESCRIPTIVE_ONLY` | percent (%), descriptive only |
| `date_mismatch_with_notable` | count (models) |

## `data/processed/chart6_eci_date_discrepancies.csv`

- **Source / provider:** Epoch ECI + Notable — [source register](data_sources_and_licenses.md)
- **File role:** Derived output
- **Primary key in frozen file:** `Model` (check uniqueness in future updates)
- **Rows / columns:** 22 / 6
- **Observation range / latest:** eci_year: 2023 to 2026; eci_date: 2023-03-14 to 2026-08-02
- **Source licence:** Inherited from underlying source(s), see source register
- **Transform:** Model-name matches with inconsistent dates; no date replacement

| Column | Units or meaning |
|---|---|
| `Model` | model name / record ID |
| `eci_date` | date YYYY-MM-DD |
| `notable_publication_date` | date YYYY-MM-DD |
| `eci_year` | calendar year |
| `notable_year` | calendar year |
| `year_differs` | boolean indicator (0/1) |

## `data/processed/chart6_eci_notable_exact_join.csv`

- **Source / provider:** Epoch ECI + Notable — [source register](data_sources_and_licenses.md)
- **File role:** Derived output
- **Primary key in frozen file:** `Model` (check uniqueness in future updates)
- **Rows / columns:** 277 / 19
- **Observation range / latest:** eci_year: 2023 to 2026; eci_date: 2023-02-24 to 2026-10-07
- **Source licence:** Inherited from underlying source(s), see source register
- **Transform:** Exact-name join from ECI to Notable; add training compute and match flags

| Column | Units or meaning |
|---|---|
| `Model` | model name / record ID |
| `Display name` | human-readable model name |
| `eci_date` | date YYYY-MM-DD |
| `eci_year` | calendar year |
| `eci` | ECI score (index units) |
| `eci_ci_low` | ECI score, lower confidence bound |
| `eci_ci_high` | ECI score, upper confidence bound |
| `eci_country` | country tags |
| `eci_organization` | organisation name(s) |
| `eci_accessibility` | category |
| `exact_name_match` | boolean indicator (0/1) |
| `notable_date` | date YYYY-MM-DD |
| `notable_country` | country tags |
| `notable_domain` | category |
| `notable_training_compute_flop` | FLOP |
| `compute_available` | boolean indicator (0/1) |
| `notable_org` | organization |
| `eci_country_tags` | US/China tags |
| `notable_country_tags` | US/China tags |

## `data/processed/chart6_eci_unmatched_review.csv`

- **Source / provider:** Epoch ECI + Notable — [source register](data_sources_and_licenses.md)
- **File role:** Derived output
- **Primary key in frozen file:** `ECI_Model` (check uniqueness in future updates)
- **Rows / columns:** 166 / 7
- **Observation range / latest:** ECI_date: 2023-02-24 to 2026-10-07
- **Source licence:** Inherited from underlying source(s), see source register
- **Transform:** Unmatched ECI names with tentative text suggestions, not accepted as links

| Column | Units or meaning |
|---|---|
| `ECI_Model` | model name |
| `ECI_date` | date YYYY-MM-DD |
| `ECI_country` | country tag |
| `suggested_notable_name_1` | possible name match |
| `suggested_notable_name_2` | possible name match |
| `review_status` | review workflow label |
| `notes` | text |

## `data/processed/chart6_eci_us_china_full_country_scores.csv`

- **Source / provider:** Epoch ECI — [source register](data_sources_and_licenses.md)
- **File role:** Derived output
- **Primary key in frozen file:** `Model + country` (check uniqueness in future updates)
- **Rows / columns:** 237 / 8
- **Observation range / latest:** year: 2023 to 2026; release_date: 2023-02-24 to 2026-10-07
- **Source licence:** Inherited from underlying source(s), see source register
- **Transform:** Country-tag US/China ECI scores; includes models without Notable match

| Column | Units or meaning |
|---|---|
| `Model` | model name / record ID |
| `country` | US or China label |
| `release_date` | date YYYY-MM-DD |
| `year` | calendar year |
| `eci` | ECI score (index units) |
| `eci_ci_low` | ECI score, lower confidence bound |
| `eci_ci_high` | ECI score, upper confidence bound |
| `accessibility` | access category |

## `data/processed/owid_us_china_2016_2024.csv`

- **Source / provider:** CSET via OWID — [source register](data_sources_and_licenses.md)
- **File role:** Derived output
- **Primary key in frozen file:** `year + country` (check uniqueness in future updates)
- **Rows / columns:** 18 / 4
- **Observation range / latest:** year: 2016 to 2024
- **Source licence:** Inherited from underlying source(s), see source register
- **Transform:** Filter United States and China, 2016–2024; preserve source publication counts

| Column | Units or meaning |
|---|---|
| `year` | calendar year |
| `country` | US or China label |
| `country_code` | ISO3 |
| `ai_publications` | publications/year |

## `data/raw/annual-scholarly-publications-on-artificial-intelligence.csv`

- **Source / provider:** CSET via OWID — [source register](data_sources_and_licenses.md)
- **File role:** Original, unmodified source data
- **Primary key in frozen file:** `Entity + Year` (check uniqueness in future updates)
- **Rows / columns:** 1,613 / 4
- **Observation range / latest:** Year: 2016 to 2024
- **Source licence:** raw metadata / underlying CSET (CC BY-NC 4.0)
- **Transform:** None; publisher data downloaded directly

| Column | Units or meaning |
|---|---|
| `Entity` | geographic entity (categorical) |
| `Code` | ISO 3-letter code / regional code |
| `Year` | calendar year |
| `AI scholarly publications - Field: All` | publications/year |

## `data/raw/epoch_eci_model_scores_20261020.csv`

- **Source / provider:** Epoch AI ECI model scores — [source register](data_sources_and_licenses.md)
- **File role:** Original, unmodified source data
- **Primary key in frozen file:** `Model` (check uniqueness in future updates)
- **Rows / columns:** 277 / 11
- **Observation range / latest:** date: 2023-02-24 to 2026-10-07
- **Source licence:** Epoch AI (CC BY)
- **Transform:** None; archived download

| Column | Units or meaning |
|---|---|
| `Model` | model name / record ID |
| `Display name` | human-readable model name |
| `eci` | ECI score (index units) |
| `eci_ci_low` | ECI score, lower confidence bound |
| `eci_ci_high` | ECI score, upper confidence bound |
| `date` | date YYYY-MM-DD |
| `Organization` | organisation name(s) |
| `Country (of organization)` | country names; may be multi-valued |
| `Model accessibility` | model access categories; may be multi-valued |
| `Accessibility group` | access category |
| `model_versions` | model version identifiers |

## `data/raw/epoch_notable_ai_models_20261020.csv`

- **Source / provider:** Epoch AI Notable Models — [source register](data_sources_and_licenses.md)
- **File role:** Original, unmodified source data
- **Primary key in frozen file:** `Model` (check uniqueness in future updates)
- **Rows / columns:** 1,078 / 47
- **Observation range / latest:** Publication date: 1950-07-02 to 2026-09-30
- **Source licence:** Epoch AI (CC BY)
- **Transform:** None; archived download

| Column | Units or meaning |
|---|---|
| `Model` | model name / record ID |
| `Organization` | organisation name(s) |
| `Publication date` | date YYYY-MM-DD |
| `Domain` | model domain / category |
| `Task` | task name / category |
| `Parameters` | parameters (check Epoch unit conventions) |
| `Parameters notes` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Training compute (FLOP)` | FLOP (total training compute) |
| `Training compute notes` | text notes |
| `Training dataset` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Training dataset size (total)` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Dataset size notes` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Confidence` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Link` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Reference` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Citations` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Authors` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Abstract` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Organization categorization` | Epoch organisation tags, may be multi-valued |
| `Country (of organization)` | country names; may be multi-valued |
| `Notability criteria` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Notability criteria notes` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Epochs` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Training time (hours)` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Training time notes` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Training hardware` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Hardware quantity` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Hardware utilization (MFU)` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Training compute cost (2023 USD)` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Compute cost notes` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Training power draw (W)` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Base model` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Finetune compute (FLOP)` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Finetune compute notes` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Batch size` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Batch size notes` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Model accessibility` | model access categories; may be multi-valued |
| `Training code accessibility` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Inference code accessibility` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Accessibility notes` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Numerical format` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Frontier model` | model frontier flag per Epoch definition |
| `Hardware acquisition cost` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Hardware utilization (HFU)` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Training compute cost (cloud)` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Training compute cost (upfront)` | Source-defined field; see Epoch documentation (unit may be model-specific) |
| `Open model weights?` | Source-defined field; see Epoch documentation (unit may be model-specific) |

