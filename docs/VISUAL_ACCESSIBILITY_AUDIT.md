# Visual-accessibility and browser acceptance audit

**Baseline:** Streamlit-hosted static HTML pages, frozen Epoch/CSET snapshot 20 October 2026. GitHub Actions workflow in .github/workflows/portfolio-checks.yml runs Playwright/Chromium against the actual Streamlit HTTP server.

## Browser verification

- Every one of the eight pages (Introduction, six chapters, Conclusion) was loaded in Chromium at **1366×768**.
- Warm local page timings on the first successful complete run were **0.614–0.668 seconds** (these timings include an intentional ~600 ms post-DOM readiness delay). They are *not* a Streamlit Community Cloud cold-start claim.
- Every desktop page was checked for document width no greater than viewport width.
- Chapter 3 Top 5, Chapter 5 filters present, Chapter 6 model name selector, scatter hover and no-match model search were exercised. The Streamlit host iframe and chapter link were also tested.
- Mobile screenshot captures are stored as an artifact in the latest successful GitHub Actions workflow. Additional mobile overflow checks are logged as warnings.
- The native Streamlit app offers a **Show exact data table** control per chapter, allowing values to be read without mouse hovering.

## Colour/contrast verification

The primary US/China colour codes are **#286DB7 (US blue)** and **#D55D36 (China orange-red)**. Chart 2 uses a closely related blue/orange palette. Country names are also printed in headings, legends and model tables; colour alone is not the sole indicator.

A simple approximate matrix simulation (scripts/check_colour_vision.py) gave:
| Approximate simulation | US RGB | China RGB | Euclidean RGB distance |
|---|---|---|---:|
| Protanopia | 70,70,165 | 161,160,63 | 163.7 |
| Deuteranopia | 66,61,161 | 168,177,66 | 181.3 |
| Tritanopia | 43,151,148 | 207,71,73 | 197.3 |

On the site paper background (#FAF9F5), US blue has approximately **5.03:1** contrast and China orange approximately **3.66:1**. The orange meets the **3:1 large-heading** threshold, not the 4.5:1 normal-sized text threshold; keep small labels in the dark text colour and use orange primarily for large headings, bars and dots.

**Scope note:** These are approximate numeric simulation matrices and static visual checks, not a formal WCAG certification or clinical colour-vision emulator. Functional labels and alternative data tables remain essential. The live public Streamlit Cloud instance must still be tested after deployment.
