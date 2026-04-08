import asyncio
import re
from playwright.async_api import async_playwright, expect

from utils.steps import async_step


async def playwright_page_open(page, request):
    async def action():
        await page.goto("https://playwright.dev", wait_until="domcontentloaded")
        await page.wait_for_load_state("networkidle")

    await async_step(page, "Open Playwright home page", action, request)


async def playwright_py(page, request):
    async def action():
        await page.get_by_role("button", name="Node.js").wait_for(state="visible", timeout=60_000)
        await page.get_by_role("button", name="Node.js").click()

        python_link = page.get_by_label("Main").get_by_role("link", name="Python")
        await python_link.wait_for(state="visible", timeout=60_000)
        await python_link.click()

        await expect(page).to_have_url(re.compile(r"^https://playwright\.dev/python/?$"), timeout=60_000)

    await async_step(page, "Switch documentation to Python", action, request)


async def playwright_node(page, request):
    async def action():
        await page.get_by_role("button", name="Python").wait_for(state="visible", timeout=60_000)
        await page.get_by_role("button", name="Python").click()

        node_link = page.get_by_label("Main").get_by_role("link", name="Node.js")
        await node_link.wait_for(state="visible", timeout=60_000)
        await node_link.click()

        await page.goto("https://playwright.dev/docs/intro", wait_until="domcontentloaded")
        await expect(page).to_have_url(re.compile(r"playwright\.dev/docs/"), timeout=60_000)

    await async_step(page, "Switch documentation back to Node.js", action, request)


async def run_scenario(request):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, slow_mo=100)
        context = await browser.new_context()
        page = await context.new_page()

        await playwright_page_open(page, request)
        await playwright_py(page, request)
        await playwright_node(page, request)

        await browser.close()


def test_playwright_navigation(request):
    asyncio.run(run_scenario(request))