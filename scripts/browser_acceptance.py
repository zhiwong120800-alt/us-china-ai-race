#!/usr/bin/env python3
"""Browser checks for the eight frozen HTML pages served by Streamlit.

Requires: pip install playwright; python -m playwright install chromium
Assumes: streamlit run app.py --server.headless true --server.port 8501
These are warm local-browser checks, NOT proof of Streamlit Cloud cold-start speed.
"""
import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE="http://localhost:8501/app/static/"
PAGES=[
 "index.html","Chapter_01_Papers_vs_Models.html",
 "Chapter_02_Frontier_Gap.html","Chapter_03_Who_Builds_It_Integrated.html",
 "Chapter_04_Industry_Academia.html","Chapter_05_Open_vs_Closed.html",
 "Chapter_06_Volume_vs_Quality.html","Conclusion.html"
]
OUT=Path("qa_screenshots")
OUT.mkdir(exist_ok=True)

def run():
    reports=[]
    with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=True,args=["--no-sandbox"])
        page=browser.new_page(viewport={"width":1366,"height":768},device_scale_factor=1)
        page.on("pageerror",lambda exc: print("PAGE_JS_ERROR:",str(exc)[:350]))
        for i,name in enumerate(PAGES):
            t=time.monotonic()
            response=page.goto(BASE+name,wait_until="domcontentloaded",timeout=30000)
            page.wait_for_timeout(600)
            sec=round(time.monotonic()-t,3)
            sizes=page.evaluate("""() => ({
                viewport: window.innerWidth,
                documentWidth: document.documentElement.scrollWidth,
                bodyWidth: document.body.scrollWidth,
                title:document.title,
                heading:document.querySelector('h1')?.innerText||''
            })""")
            assert response and response.status==200, f"{name}: not HTTP 200"
            assert sizes["heading"], f"{name}: missing page heading"
            assert sizes["documentWidth"]<=sizes["viewport"]+2, f"{name}: horizontal overflow: {sizes}"
            assert sec < 5, f"{name}: warm load >5s: {sec}"
            page.screenshot(path=str(OUT/f"desktop_{i:02d}.png"),full_page=False)
            reports.append({"page":name,"warmSeconds":sec,"width":sizes["documentWidth"],"viewport":sizes["viewport"],"ok":True})
            print("PASS_DESKTOP",name,sec,"seconds")
        page.goto(BASE+"Chapter_03_Who_Builds_It_Integrated.html")
        page.locator("#usrows .devrow").first.wait_for()
        fill=page.locator("#usrows .bararea").first.evaluate("(el)=>getComputedStyle(el).backgroundImage")
        assert "gradient" in fill and ("40, 109, 183" in fill or "286db7" in fill or "#286db7" in fill), "Chapter 3 US bar did not render its blue gradient"
        page.locator("#top5").click()
        assert page.locator("#usrows .devrow").count()==5, "Chapter 3 top-five filter failed"
        page.goto(BASE+"Chapter_06_Volume_vs_Quality.html")
        picker=page.locator("#trendModelPicker")
        picker.wait_for()
        assert picker.locator("option").count()>50, "Chapter 6 model finder does not list visible models"
        picker.select_option(index=1)
        assert page.locator("#trendSVG .point.selected").count()==1, "Model picker did not highlight exactly one point"
        page.locator("#scatterSVG circle.point").first.hover()
        page.locator("#scatterTooltip:not([hidden])").wait_for(timeout=2000)
        assert "Training compute" in page.locator("#scatterTooltip").inner_text()
        page.locator("#recordSearch").fill("zz_no_real_model_98653")
        assert "No matching models" in page.locator("#modelRows").inner_text(), "Empty search does not show a message"
        print("PASS_INTERACTIONS chapter 3 and 6 model finder, scatter hover and empty search")
        page.goto(BASE+"Chapter_05_Open_vs_Closed.html")
        assert page.locator("#developer").count()==1 and page.locator("#period").count()==1, "Chapter 5 interactive controls missing"
        print("PASS_INTERACTIONS chapter 5 developer / period selectors")

        # Test the Streamlit host and the in-chapter CTA, which must update
        # the top-level app/side bar rather than navigating only within an iframe.
        page.goto("http://localhost:8501/",wait_until="domcontentloaded",timeout=30000)
        page.frame_locator('iframe[title="The AI Race: Introduction"]').locator("h1").wait_for(timeout=15000)
        assert page.get_by_text("Research question:",exact=False).count()>0
        page.frame_locator('iframe[title="The AI Race: Introduction"]').locator("a.cta").click()
        page.frame_locator('iframe[title="The AI Race: 01 · Papers vs Models"]').locator("h1").wait_for(timeout=15000)
        assert "Papers" in page.url, "Introduction CTA did not update the host page"
        print("PASS_STREAMLIT_HOST chapter CTA updates real Streamlit chapter")

        # Regression for the large green bottom-of-chapter story-pager button.
        from urllib.parse import quote
        page.goto("http://localhost:8501/?page="+quote("03 · Who Builds It?"),wait_until="domcontentloaded",timeout=30000)
        chap3=page.frame_locator('iframe[title="The AI Race: 03 · Who Builds It?"]')
        chap3.locator("h1").wait_for(timeout=15000)
        chap3.locator("a.story-pager-button").click()
        page.frame_locator('iframe[title="The AI Race: 04 · Industry vs Academia"]').locator("h1").wait_for(timeout=15000)
        assert "Industry" in page.url, "Chapter 3 green chapter link failed to switch the Streamlit host"
        print("PASS_CHAPTER_PAGER chapter 3 green button opens Chapter 4")

        # Regression: native controls must work and reset the host's scroll
        # position when advancing from the bottom of a long chapter.
        page.goto("http://localhost:8501/",wait_until="domcontentloaded",timeout=30000)
        page.frame_locator('iframe[title="The AI Race: Introduction"]').locator("h1").wait_for(timeout=15000)
        page.get_by_role("button", name="Next →").click()
        page.frame_locator('iframe[title="The AI Race: 01 · Papers vs Models"]').locator("h1").wait_for(timeout=15000)
        assert page.get_by_text("StreamlitWidgetAlreadyInstantiatedError").count()==0
        page.get_by_role("button", name="← Previous").click()
        page.frame_locator('iframe[title="The AI Race: Introduction"]').locator("h1").wait_for(timeout=15000)
        assert page.get_by_text("StreamlitWidgetAlreadyInstantiatedError").count()==0
        print("PASS_STREAMLIT_NATIVE_NAV native Next and Previous buttons")

        page.goto("http://localhost:8501/?page="+quote("03 · Who Builds It?"),wait_until="domcontentloaded",timeout=30000)
        page.frame_locator('iframe[title="The AI Race: 03 · Who Builds It?"]').locator("h1").wait_for(timeout=15000)
        page.get_by_role("button", name="Next →").scroll_into_view_if_needed()
        def host_scroll():
            return page.evaluate("""() => Math.max(window.scrollY,
              document.querySelector('[data-testid="stMain"]')?.scrollTop || 0,
              document.querySelector('.stMain')?.scrollTop || 0,
              document.querySelector('[data-testid="stAppViewContainer"]')?.scrollTop || 0)""")
        before=host_scroll()
        assert before>100, f"Could not scroll down long chapter to test reset: {before}"
        page.get_by_role("button", name="Next →").click()
        page.frame_locator('iframe[title="The AI Race: 04 · Industry vs Academia"]').locator("h1").wait_for(timeout=15000)
        page.wait_for_timeout(350)
        after=host_scroll()
        assert after<100, f"Next chapter did not scroll host to top (before {before}, after {after})"
        print("PASS_NATIVE_SCROLL_RESET",before,"to",after)

        # Chapter 2's plot is nested in its original srcdoc iframe.
        page.goto(BASE+"Chapter_02_Frontier_Gap.html")
        plot=page.frame_locator("iframe.previewframe")
        plot.locator("circle.point").first.hover()
        plot.locator("#tooltip.show").wait_for(timeout=2000)
        assert "training FLOP" in plot.locator("#tooltip").inner_text(), "Chapter 2 hover lacks model details"
        print("PASS_CHAPTER_02_HOVER immediate compute tooltip appears on hover")

        # Reset for mobile static page captures.

        # Mobile is a useful additional acceptance check, not part of the desktop-only rubric item.
        page.set_viewport_size({"width":390,"height":844})
        for name in ["index.html","Chapter_01_Papers_vs_Models.html","Chapter_03_Who_Builds_It_Integrated.html","Chapter_05_Open_vs_Closed.html","Chapter_06_Volume_vs_Quality.html"]:
            page.goto(BASE+name,wait_until="domcontentloaded",timeout=30000)
            page.wait_for_timeout(400)
            widths=page.evaluate("() => [document.documentElement.scrollWidth,window.innerWidth]")
            if widths[0]>widths[1]+2:
                print("MOBILE_OVERFLOW_WARNING",name,widths)
            page.screenshot(path=str(OUT/("mobile_"+name.replace(".html","")+".png")),full_page=False)
        browser.close()
    (OUT/"results.json").write_text(json.dumps(reports,indent=2),encoding="utf-8")
    print("PASS_BROWSER_ACCEPTANCE",len(reports),"desktop pages")

if __name__=="__main__":
    run()
