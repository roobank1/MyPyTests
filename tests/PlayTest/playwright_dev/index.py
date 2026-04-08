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
      
    
async def playwright_search(page, request, search_value):
    async def action():
        await page.get_by_role("button", name="Search (Ctrl+K)").click()
        await page.get_by_role("searchbox", name="Search").fill(search_value)
        await page.get_by_role("link", name="Python Supported languages").click()
        await page.get_by_role("link", name="GitHub repo").nth(2).click()
        await page.wait_for_timeout(1000)
    await async_step(page, f"Perform search for '{search_value}' and open GitHub repo", action, request)


