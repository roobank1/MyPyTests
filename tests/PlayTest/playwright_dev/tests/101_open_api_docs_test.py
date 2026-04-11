
from asyncio import run
from playwright.async_api import async_playwright
from tests.PlayTest.playwright_dev.pages.index_page import IndexPage

# Scenario runner for test
async def run_scenario(request):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        index = IndexPage(page, request)
        await index.open()
        await index.open_api()
        await browser.close()

def test_playwright_navigation(request):
    run(run_scenario(request))