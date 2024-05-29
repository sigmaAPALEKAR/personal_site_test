from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://joshuamae.com")
        assert page.title() == "Joshua Mae"
        browser.close()
