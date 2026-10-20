# Source register, versions and licence notes

Snapshot frozen for the group on **2026-10-20**. See `docs/source_checksums.sha256` for cryptographic file checksums. Dates below are based on bundled metadata; source websites may change after the snapshot.

| Source | Upstream source / source URL | Raw file | Licensing / attribution | Time coverage and freshness |
|---|---|---|---|---|
| Epoch AI — Notable AI Models | [Epoch AI model dataset](https://epoch.ai/data/ai-models) and [dataset documentation](https://epoch.ai/data/ai-models-documentation) | `data/raw/epoch_notable_ai_models_20261020.csv` | Creative Commons Attribution (CC BY), credit Epoch AI. Refer to source page for full terms. | Publication dates extend to 2026-09-30 in frozen snapshot; historical coverage is broader than project's main analysis |
| Our World in Data — Annual scholarly publications on AI | [OWID grapher](https://ourworldindata.org/grapher/annual-scholarly-publications-on-artificial-intelligence); underlying CSET [Country Activity Tracker](https://cat.eto.tech/) | `data/raw/annual-scholarly-publications-on-artificial-intelligence.csv` plus `.metadata.json` and source `readme.md` | **Underlying CSET data: CC BY-NC 4.0** ([CSET terms](https://eto.tech/tou/)); attribute CSET and OWID. Do not assume OWID-wide licensing supersedes upstream terms. | 2016–2024; metadata records last data update 2026-04-27 |
| Epoch AI — Epoch Capabilities Index | [ECI](https://epoch.ai/eci) | `data/raw/epoch_eci_model_scores_20261020.csv` | Source describes use under Creative Commons Attribution (CC BY 4.0); retain Epoch AI attribution and verify licence terms before any public redistribution. | ECI model publication dates through 2026-10-07 in frozen snapshot |

## Attribution on figures

- **Paper count:** 'Source: CSET (2026), via Our World in Data; 2016–2024; excludes research without an English title/abstract.'
- **Notable models and compute:** 'Source: Epoch AI, Data on AI Models; group snapshot 20 Oct 2026; selected notable models, not a census.'
- **Capability:** 'Source: Epoch AI, Epoch Capabilities Index; group snapshot 20 Oct 2026; benchmark-evaluated models.'

## Important restrictions and caveats

1. The project is a university coursework exercise. CSET's **NonCommercial** restriction still applies when sharing derived artifacts. Check permissions before using these data in commercial settings.
2. Preserve original source metadata and source filenames; do not replace raw snapshots with new downloads.
3. Notable model counts, ECI benchmark scores, and paper counts are distinct populations and units. Do not calculate a paper-to-model conversion rate or imply that more training FLOPs proves better downstream model ability.
4. Whole counting: a model or paper associated with both US and China can count in both countries. Country shares therefore refer to the two countries' counts, *not* global shares.
5. The ECI–Notable join is **exact-name only**; review candidates are not accepted matches. Refer to `docs/eci_matching_audit_20261020.md`.

## Data refresh tracking

- Raw files frozen locally: **2026-10-20**.
- OWID data's own last updated date: **2026-04-27**.
- For public Streamlit app show both **snapshot date** and **source-specific latest observation**, not a single misleading '2026' label.
