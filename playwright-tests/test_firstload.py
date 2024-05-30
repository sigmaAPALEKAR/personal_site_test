from playwright.sync_api import sync_playwright

def test_firstload(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)  
        page = browser.new_page()
        page.goto("https://joshuamae.com")
        title = page.title()
        assert title == "Joshua Mae", f"Title was '{title}', but expected 'Joshua Mae'"
        browser.close()

def main():
    browsers = ["chromium", "firefox", "webkit"]
    for browser_type in browsers:
        print(f"Testing on {browser_type}...")
        test_example(browser_type)

if __name__ == "__main__":
    main()