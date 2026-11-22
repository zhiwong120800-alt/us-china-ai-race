# Final Part 2 submission checklist

The rubric is **30 binary checks (six groups of six)**. This is a preparation checklist, **not** evidence that a deployment or group approval has occurred.

## Machine-verifiable
- [ ] The latest main GitHub Actions portfolio-checks workflow passes.
- [ ] Raw source checksums remain unchanged; all generated data/processed tables match rebuilds.
- [ ] The frozen SHA contains app.py, static/ (8 HTML files), data/raw, data/review, data/processed, docs/data_dictionary.md, and the disclosure/matrix.
- [ ] Six chapters present at the live Streamlit app; all native navigation works.
- [ ] The opening page states the research question and persona.

## Browser acceptance (1366 × 768)
- [ ] Page load measured at less than 5 seconds under the assessment environment (cold starts must be reported separately).
- [ ] At least two filters refresh visually in about one second.
- [ ] Empty result selections display an informative message.
- [ ] No horizontal page scroll; content readable with vertical scrolling.
- [ ] Axes and legends include units; every value accessible without hover (data tables, labels, click details).
- [ ] Check US blue / China orange at common colour-vision deficiency simulations; preserve clear text/categorical labels.
- [ ] Review responsive layouts including the Chapter 2/4 nested iframes.

## Human and submission
- [ ] Aditi and Manasvi contribute verified, factual AI provenance rows.
- [ ] All members approve docs/data_ai_disclosure.md.
- [ ] Streamlit Community Cloud publicly deploys this EXACT main commit.
- [ ] Create one PDF listing: live Streamlit URL; repository URL; immutable graded commit SHA.
- [ ] Confirm Canvas deadline, because the text contains conflicting Friday and Monday dates.

See docs/STREAMLIT_DEPLOYMENT.md for the cloud steps. Never replace the submitted SHA with the mutable main branch name in the PDF.
