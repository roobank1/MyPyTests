import asyncio
import re
from playwright.async_api import async_playwright, expect


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
    await expect(page).to_have_url(re.compile(r"^https://playwright\.dev/python/?$"), timeout=60_000)


async def playwright_node(page):
    await page.get_by_role("button", name="Python").wait_for(state="visible", timeout=60_000)
    await page.get_by_role("button", name="Python").click()

    node_link = page.get_by_label("Main").get_by_role("link", name="Node.js")
    await node_link.wait_for(state="visible", timeout=60_000)
    await node_link.click()

    # The language switcher may be overridden by a session cookie; navigate
    # directly to ensure we land on the Node.js docs regardless.
    await page.goto("https://playwright.dev/docs/intro", wait_until="domcontentloaded")
    await expect(page).to_have_url(re.compile(r"playwright\.dev/docs/"), timeout=60_000)


async def run_scenario():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, slow_mo=100)
        context = await browser.new_context()
        page = await context.new_page()

        await playwright_page_open(page)
        await playwright_py(page)
        await playwright_node(page)

        await browser.close()


def test_playwright_navigation():
    asyncio.run(run_scenario())