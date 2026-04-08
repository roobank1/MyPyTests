import asyncio
from playwright.async_api import async_playwright

from utils.steps import async_step

async def playwright_page_open(page, request):
    async def action():
        await page.goto("https://playwright.dev")
    await async_step(page, "Open Playwright home page", action, request)
    
    
async def playwright_py(page, request):
    async def action():
        await page.get_by_role("button", name="Node.js").click()
        await page.get_by_label("Main").get_by_role("link", name="Python").click()
        await page.wait_for_timeout(1000)
    await async_step(page, "Switch documentation to Python", action, request)


async def playwright_node(page, request):
    async def action():
        await page.get_by_role("button", name="Python").click()
        await page.get_by_label("Main").get_by_role("link", name="Node.js").click()
        await page.wait_for_timeout(1000)
    await async_step(page, "Switch documentation back to Node.js", action, request)
    
    
async def playwright_api(page, request):
    async def action():
        await page.get_by_role("link", name="API").click()
        await page.get_by_role("link", name="errors", exact=True).click()
        await page.wait_for_timeout(1000)
    await async_step(page, "Click API documentation link", action, request)    


async def run_scenario(request):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, slow_mo=100)
        context = await browser.new_context()
        page = await context.new_page()

        await playwright_page_open(page, request)
        await playwright_py(page, request)
        await playwright_node(page, request)
        await playwright_api(page, request)

        await browser.close()


def test_playwright_navigation(request):
    asyncio.run(run_scenario(request))