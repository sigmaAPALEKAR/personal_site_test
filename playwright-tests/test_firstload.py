import pytest
from playwright.async_api import async_playwright

@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
async def test_firstload(browser_name, browser_type, context):
    browser = await browser_type.launch()
    page = await context.new_page()
    await page.goto("https://joshuamae.com")
    title = await page.title()
    assert title == "Joshua Mae", f"Title was '{title}', but expected 'Joshua Mae'"
    await browser.close()