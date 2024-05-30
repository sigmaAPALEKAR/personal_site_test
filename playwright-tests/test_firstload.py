import pytest
from playwright.async_api import Page, Browser

@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
async def test_firstload(browser_name, browser_type_launch):
    browser: Browser = await browser_type_launch(browser_name)
    context = await browser.new_context()
    page: Page = await context.new_page()
    await page.goto("https://example.com")
    title = await page.title()
    assert title == "Example Domain", f"Title was '{title}', but expected 'Example Domain'"
    await browser.close()
