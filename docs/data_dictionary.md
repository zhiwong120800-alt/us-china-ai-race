# Data dictionary — frozen snapshot, with audited Chart 3–5 additions (20 Oct 2026)

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


---

## Audited Chart 3–5 data files (added to the final portfolio)

**Shared provenance and licence:** All records derive from Epoch AI Notable Models (https://epoch.ai/data/ai-models), frozen **20 October 2026**, original source licensed under CC BY according to the source register. The *review* CSVs include student-assigned classifications and attribution decisions. Treat those decisions as interpretive input; they are not automatically verified facts about organisation ownership. The latest original Notable model publication date is **30 September 2026**, but these chapter analyses restrict years to **2016–2025**. Source rows can include a model in both countries. Reconstruct using **python scripts/rebuild_chapter_data.py**.

### data/review/chart3_model_attribution_review.csv
- **Source / URL / licence:** Epoch AI Notable Models; https://epoch.ai/data/ai-models; CC BY + reviewed team country attribution.
- **Key:** model + country; **Rows:** 679. Of these, 667 are US/China and 12 are optional Hong Kong sensitivity rows.
- **Time / latest:** 2016–2025, latest observation 2025.
- **Fields:** model (name/identifier), country (country tag), year (calendar year), publication_date (ISO date), alignment (mapping provenance label).
- **Transform:** Frozen reviewed model–country attribution saved from the published Chapter 3 model-level payload; cross-check the country/model denominators against Charts 4–5.

### data/review/chart3_affiliation_review.csv
- **Source / URL / licence:** Epoch AI Notable Models; https://epoch.ai/data/ai-models; CC BY + manually reviewed organisation aliases.
- **Key:** model + country + developer; **Rows:** 909.
- **Time / latest:** 2016–2025, latest observation 2025.
- **Fields:** model (identifier), country (country tag), year (calendar year), developer (original organisation label), family (audited grouped-organisation label).
- **Transform:** Frozen reviewed participation mapping from Chapter 3. Multiple developer rows may point to one model; concentration uses the **union of distinct models**, not the sum of organisation bar counts.

### data/review/chart3_org_mapping_review.csv
- **Source / URL / licence:** Epoch AI organisation labels; https://epoch.ai/data/ai-models; CC BY + group review annotations.
- **Key:** org; **Rows:** 26 explicitly recorded organisation review decisions.
- **Time / latest:** Applied to frozen source through 2026-09-30; chart visual period through 2025.
- **Fields:** org (source organisation name), country (reviewed original country), parent (organisation grouping), evidence (reason/trace), rule (grouping decision).
- **Transform:** Recorded manual decisions used to reconstruct the full source-label mapping.

### data/review/chart4_developer_type_review.csv
- **Source / URL / licence:** Epoch AI Notable Models; https://epoch.ai/data/ai-models; CC BY + group-authored developer-type classification.
- **Key:** Model + country; **Rows:** 667 (US 514, China 153).
- **Time / latest:** 2016–2025, latest observation 2025.
- **Fields:** Model (name), Organization (raw organisation name(s)), Publication date (ISO date), country (US or China), period (2016–19, 2020–22, 2023–25), category (Industry, Academia, Collaboration, Other, Unknown).
- **Transform:** Human-reviewed mutually exclusive developer type used in Chapter 4 and reused in Chapter 5. Checked model/date/organisation/country against raw source.

### data/review/chart5_release_review.csv
- **Source / URL / licence:** Epoch AI Notable Models; https://epoch.ai/data/ai-models; CC BY + group-authored release/access classification.
- **Key:** model + country; **Rows:** 667.
- **Time / latest:** 2016–2025, latest observation 2025.
- **Fields:** model (name), organisation (raw name(s)), publication_date (ISO date), year (calendar year), country (US/China), period (calendar interval), developer_type (shared Chart 4 type), release_strategy (Open weights / API or hosted / Unreleased / Unknown), source_accessibility (original Epoch source category).
- **Transform:** Reviewed model-level classifications saved from Chapter 5's 667-record interactive payload. The original field is preserved to audit category decisions.

### data/processed/chart3_model_country.csv and chart3_affiliations.csv
- **Source / URL / licence:** Frozen Epoch data plus reviewed inputs above; https://epoch.ai/data/ai-models; CC BY + human-reviewed mappings.
- **Keys / units / coverage:** Same keys, columns, units, latest observation and row counts as their respective review inputs (679 and 909 rows).
- **Transform:** Recreated from the reviewed country- and developer-attribution inputs by scripts/rebuild_chapter_data.py, with consistency checks against the 667 US/China model–country pairs used by Chapters 4–5.

### data/processed/chart3_org_map.csv
- **Source / URL / licence:** Frozen Epoch organisation names + explicit review mappings; https://epoch.ai/data/ai-models; CC BY + team annotations.
- **Key:** org (unique original organisation label); **Rows:** 372 distinct nonempty raw labels under literal comma-separated parsing.
- **Time / latest:** Raw source through 2026-09-30; chapter analysis 2016–2025.
- **Fields:** org (raw label), country (source/reviewed organisation country, blank if ambiguous), parent (grouped label), evidence (trace), rule (classification decision), status (explicit_review / derived_from_chapter_3 / unreviewed_original_label).
- **Transform:** Raw source-label extraction + audited parent mapping, with unreviewed rows explicitly marked. Original online documentation referred to 371 organisations under a different/unspecified counting treatment; this table uses reproducible literal parsing and **does not assert all 372 labels received manual review**.

### data/processed/chart4_model_type_records.csv
- **Source / URL / licence:** Epoch + Chart 4 reviewed classification; https://epoch.ai/data/ai-models; CC BY + reviewed input.
- **Key / rows / columns / units / coverage:** Same as chart4_developer_type_review.csv: Model + country, 667 rows, 2016–2025.
- **Transform:** Rebuilt and source-validated from the Chart 4 review table.

### data/processed/chart4_period_summary.csv
- **Source / URL / licence:** Epoch + Chart 4 reviewed classification; https://epoch.ai/data/ai-models; CC BY + reviewed input.
- **Key:** country + period; **Rows:** 6, US/China × three fixed periods.
- **Time / latest:** 2016–2025; latest 2023–25 interval.
- **Fields:** country (US/China), period (fixed 4/3/3-year group), Industry/Academia/Collaboration/Other/Unknown (counts of model–country records), Total (records, integer).
- **Transform:** Group the mutually exclusive model-level category records by country and period; each category count sums to Total. Periods are unequal in duration and must not be treated as equally sized annual bins.

### data/processed/chart5_model_access_records.csv
- **Source / URL / licence:** Epoch + Chart 5 reviewed classification; https://epoch.ai/data/ai-models; CC BY + reviewed input.
- **Key / rows / columns / units / coverage:** Same as chart5_release_review.csv: model + country, 667 rows, 2016–2025.
- **Transform:** Rebuilt and source-validated from the Chart 5 review table and cross-checked against Chart 4 developer types.

### data/processed/chart5_release_strategies.csv
- **Source / URL / licence:** Epoch + Chart 5 review; https://epoch.ai/data/ai-models; CC BY + reviewed input.
- **Key:** Year + Country + Release_Strategy; **Time / latest:** 2016–2025, latest observation 2025.
- **Fields:** Year (calendar year), Country (United States/China), Release_Strategy (categorical access group), count (model–country records), total (country-year records), percentage (100 × count / total; percentage points).
- **Transform:** Group all 667 reviewed model–country records by year/country/strategy. This replaces a narrower **exact-country-string-only** pilot export in which multi-country collaborations were incorrectly omitted relative to the final website. To reproduce 2023–25 chapter percentages, aggregate counts and denominators over all three years, not annual percentages.

### data/processed/chart2_compute_models.csv
- **Source / URL / licence:** Epoch AI Notable Models, https://epoch.ai/data/ai-models; CC BY according to source register.
- **Key:** model + country; **Rows:** 375 (US 277, China 98), each with known positive training FLOPs.
- **Time / latest:** 2016-03-04 to 2026-09-09, study cutoff 2026-09-30, frozen 2026-10-20.
- **Fields / units:** model (name), country (US/China attribution), publication_date (ISO date), year (calendar year), training_compute_flop (training floating point operations, **FLOP**), compute_available (0/1 indicator, always 1 in this included subset), frontier_flag (0/1 original Epoch flag).
- **Transform:** Filter original model records to 2016-01-01 through 2026-09-30, whole-count both countries when both occur, retain positive finite source training-FLOP estimates. Script: python scripts/build_chart2.py. A reported maximum is not the global frontier.

### data/processed/chart2_compute_coverage.csv
- **Source / URL / licence:** Epoch AI Notable Models, https://epoch.ai/data/ai-models; CC BY according to source register.
- **Key:** country + year; **Rows:** 22 (2 countries × 11 years).
- **Time / latest:** calendar years 2016–2026, with 2026 right-censored at 30 September.
- **Fields / units:** country (label), year (calendar year), all_notable (country–model records, count), with_compute (records with finite positive source FLOPs, count), coverage_pct (100 × with_compute / all_notable, percent).
- **Transform:** Same frozen raw model population and whole-country attribution as the model table; include missing-FLOP records in the denominator, never as zeros. Script: python scripts/build_chart2.py.
