# Reproducibility smoke checks

From the repository root, with Python 3.10+ installed:

    python scripts/build_chart1.py
    python scripts/build_chart2.py
    python scripts/build_eci_audit.py
    python scripts/rebuild_chapter_data.py

The last command reconstructs the Chart 3/4/5 processed files from the
frozen Epoch source and the team's archived review inputs in data/review.
It asserts model identity, source organisation and publication date matches,
whole-country assignments, primary record counts, top-three concentration,
period composition, and release-category percentages.

The manual review input files are not silently treated as automatic raw
data, nor are unreviewed organisation labels presented as verified locations.

For a strict provenance audit, compare all outputs to the committed data
package after running in a clean checkout. The original source checksums
are listed in docs/source_checksums.sha256.
