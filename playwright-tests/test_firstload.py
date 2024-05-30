from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        # Test with Chromium
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://joshuamae.com")
        assert page.title() == "Joshua Mae"
        browser.close()

        # Test with Firefox
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("https://joshuamae.com")
        assert page.title() == "Joshua Mae"
        browser.close()

        # Test with WebKit
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto("https://joshuamae.com")
        assert page.title() == "Joshua Mae"
        browser.close()

# Run the test
test_example()