import asyncio
import os
from playwright.async_api import async_playwright

async def playwright_page_open(page):
    await page.goto("https://playwright.dev")
    
    
async def playwright_py(page):
    await page.get_by_role("button", name="Node.js").click()
    await page.get_by_label("Main").get_by_role("link", name="Python").click()
    await page.wait_for_url("**/python*")


async def playwright_node(page):
    await page.get_by_role("button", name="Python").click()
    await page.get_by_label("Main").get_by_role("link", name="Node.js").click()
    await page.wait_for_url("**/node*")


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