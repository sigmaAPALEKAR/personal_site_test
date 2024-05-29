import asyncio
from playwright.async_api import async_playwright

async def test_sticky_header(browser_name):
    async with async_playwright() as p:
        if browser_name == 'chromium':
            browser = await p.chromium.launch(headless=False)
        elif browser_name == 'firefox':
            browser = await p.firefox.launch(headless=False)
        elif browser_name == 'webkit':
            browser = await p.webkit.launch(headless=False)
        else:
            raise ValueError("Unsupported browser: " + browser_name)

        page = await browser.new_page()

        await page.goto('https://joshuamae.com')

        header_selector = 'header'

        await page.wait_for_selector(header_selector)

        initial_bounding_box = await page.evaluate(f'''
            () => {{
                const header = document.querySelector('{header_selector}');
                return header.getBoundingClientRect();
            }}
        ''')

        await page.evaluate('window.scrollBy(0, 1000)')
        await page.wait_for_timeout(1000)

        after_scroll_bounding_box = await page.evaluate(f'''
            () => {{
                const header = document.querySelector('{header_selector}');
                return header.getBoundingClientRect();
            }}
        ''')

        is_sticky = initial_bounding_box['top'] == after_scroll_bounding_box['top']
        assert is_sticky, f"Header is not sticky in {browser_name}."

        print(f"Sticky header test passed in {browser_name}.")

        await browser.close()

async def main():
    browsers = ['chromium', 'firefox', 'webkit']
    for browser in browsers:
        await test_sticky_header(browser)

if __name__ == "__main__":
    asyncio.run(main())
