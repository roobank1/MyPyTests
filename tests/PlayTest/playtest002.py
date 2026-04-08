import asyncio
from tests.PlayTest.playtest001 import run_scenario


def test_playwright_navigation(request):
    asyncio.run(run_scenario(request))