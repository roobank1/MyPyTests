
from asyncio import run
from playwright.async_api import async_playwright
import pytest

from tests.PlayTest.playwright_dev.pages.index_page import IndexPage


# Generic scenario runner that opens the page then runs an action coroutine
async def _run_action(request, search_value):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        index = IndexPage(page, request)
        await index.open()
        await index.search_and_open_repo(search_value=search_value)
        # await action_coro(page, request)
        await browser.close()


@pytest.mark.parametrize(
    "search_value",
    [
        "python",
        "Python",
        "PYTHON",
        "playwright",      # this will fail, as the python related results not be found in the search results
        # "playwright dev",  # this will fail, as the python related results not be found in the search results
    ],
)
def test_search_variations(request, search_value):
    run(_run_action(request, search_value))