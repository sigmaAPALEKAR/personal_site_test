from playwright.sync_api import sync_playwright

def firstload():
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto("https://joshuamae.com")
            assert page.title() == "Joshua Mae"
            browser.close()

def main():
    firstload()

if __name__ == "__main__":
    main()  