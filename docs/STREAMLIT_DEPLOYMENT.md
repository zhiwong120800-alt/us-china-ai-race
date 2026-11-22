# Streamlit Community Cloud deployment — required human action

1. Sign into https://share.streamlit.io/ with the GitHub account that has access to zhiwong120800-alt/us-china-ai-race.
2. Select **Create app** (or New app) → **Deploy a public app from GitHub**.
3. Repository: zhiwong120800-alt/us-china-ai-race
4. Branch: main
5. Main file path: app.py
6. Use a public app URL; open it in a private/incognito browser session to check public access.
7. Verify all eight sidebar entries, Chapter 02 and Chapter 04 nested charts, Chapter 05 filters, and Chapter 06 hover / model-selection controls.
8. Check the GitHub Actions reproduction job and note the precise main commit SHA that was deployed.
9. Complete AI provenance, team disclosure approval, and the single submitted PDF containing the **actual** deployed app URL (not the GitHub Pages preview).

This app uses Streamlit >=1.56 and st.iframe for eight immutable bundled HTML files. There are no API keys or secrets required for the charts; data and HTML are checked into the same GitHub commit.

If the static chapter links open in the same iframe instead of updating the sidebar radio selection, use the Streamlit native chapter navigation as the authoritative route. Both remain inside the deployed app.
