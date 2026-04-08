
from asyncio import run
from playwright.async_api import async_playwright
from tests.PlayTest.playwright_dev.index import (
    playwright_page_open,
    playwright_py,
    playwright_node,
    playwright_api,
    playwright_search,
)

# Scenario runner for test
async def run_scenario(request):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, slow_mo=100)
        context = await browser.new_context()
        page = await context.new_page()
        await playwright_page_open(page, request)
        await playwright_py(page, request)
        await playwright_node(page, request)
        await playwright_api(page, request)
        await playwright_search(page, request, search_value="python")
        await browser.close()

def test_playwright_navigation(request):
    run(run_scenario(request))