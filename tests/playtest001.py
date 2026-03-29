import asyncio
import os
from playwright.async_api import async_playwright


async def playwright_page_open(page):
    # Be explicit about load waiting for CI stability.
    await page.goto("https://playwright.dev", wait_until="domcontentloaded")
    await page.wait_for_load_state("networkidle")


async def playwright_py(page):
    # Ensure the UI is ready before interacting.
    await page.get_by_role("button", name="Node.js").wait_for(state="visible", timeout=60_000)
    await page.get_by_role("button", name="Node.js").click()

    python_link = page.get_by_label("Main").get_by_role("link", name="Python")
    await python_link.wait_for(state="visible", timeout=60_000)
    await python_link.click()

    # Default 30s can be tight on GitHub-hosted runners.
    await page.wait_for_url("**/python**", timeout=60_000)


async def playwright_node(page):
    await page.get_by_role("button", name="Python").wait_for(state="visible", timeout=60_000)
    await page.get_by_role("button", name="Python").click()

    node_link = page.get_by_label("Main").get_by_role("link", name="Node.js")
    await node_link.wait_for(state="visible", timeout=60_000)
    await node_link.click()

    await page.wait_for_url("**/node**", timeout=60_000)


async def run_scenario():
    is_ci = os.getenv("CI", "").lower() in ("true", "1", "yes")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=is_ci, slow_mo=100)
        context = await browser.new_context()
        page = await context.new_page()

        await playwright_page_open(page)
        await playwright_py(page)
        await playwright_node(page)

        await browser.close()


def test_playwright_navigation():
    asyncio.run(run_scenario())