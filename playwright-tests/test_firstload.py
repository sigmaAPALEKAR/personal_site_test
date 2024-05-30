import asyncio
from playwright.async_api import async_playwright

async def test_title(url, expected_title):
    async with async_playwright() as p:
        browsers = [
            ("Chromium", p.chromium),
            ("Firefox", p.firefox),
            ("WebKit", p.webkit)
        ]
        for browser_name, browser_type in browsers:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto(url)
            title = await page.title()

            assert title == expected_title, f"{browser_name} - Title does not match. Expected: {expected_title}, but got: {title}"

            await browser.close()
            print(f"{browser_name} - Test passed")

if __name__ == "__main__":
    url = "https://joshuamae.com.com"
    expected_title = "Joshua Mae"
    asyncio.run(test_title(url, expected_title))
