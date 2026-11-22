# Reviewed classification inputs (frozen 20 Oct 2026)

These tables are copied from the independently reviewed Chart 3/4/5 model-level payloads used in the interactive website. They are *human classification inputs*, not source data downloaded from Epoch.

Each of the 667 US/China model-country records matches the frozen 1,078-row Epoch source for model name, publication date and organisation. The 12 additional Hong Kong attribution rows in Chart 3 are optional sensitivity observations, not part of the 667 default denominator.

The 26 explicit organisation mapping decisions are in chart3_org_mapping_review.csv. The complete index of 372 raw organisation labels has been preserved in data/processed/chart3_org_map.csv, with unreviewed labels clearly identified. The earlier webpage described 371 organisations, while literal splitting of the raw Organization column yields 372 labels; these are not claimed to be identical counting definitions.

To reconstruct the derived tables, run python scripts/rebuild_chapter_data.py after installing Python 3.10+. The build script validates raw model membership and preserves original classification decisions; it does not invent new classifications.
