from utils.steps import async_step
from .base_page import BasePage


class IndexPage(BasePage):
    async def open(self):
        await self.goto("https://playwright.dev", step_name="Open Playwright home page")

    async def switch_to_python(self):
        async def action():
            await self.page.get_by_role("button", name="Node.js").click()
            await self.page.get_by_label("Main").get_by_role("link", name="Python").click()
            assert "python" in self.page.url.lower(), "URL should contain 'python'"
            await self.page.wait_for_timeout(1000)

        await async_step(self.page, "Switch documentation to Python", action, self.request)

    async def switch_to_node(self):
        async def action():
            await self.page.get_by_role("button", name="Node.js").click()
            await self.page.get_by_label("Main").get_by_role("link", name="Node.js").click()
            assert "node" in self.page.url.lower(), "URL should contain 'node'"
            await self.page.wait_for_timeout(1000)

        await async_step(self.page, "Switch documentation to Node.js", action, self.request)

    async def open_api(self):
        async def action():
            await self.page.get_by_role("link", name="API").click()
            await self.page.get_by_role("link", name="errors", exact=True).click()
            await self.page.wait_for_timeout(1000)

        await async_step(self.page, "Click API documentation link", action, self.request)

    async def search_and_open_repo(self, search_value: str):
        async def action():
            await self.page.get_by_role("button", name="Search (Ctrl+K)").click()
            await self.page.get_by_role("searchbox", name="Search").fill(search_value)
            await self.page.get_by_role("link", name="Python Supported languages").click()
            await self.page.get_by_role("link", name="GitHub repo").nth(2).click()
            await self.page.wait_for_timeout(1000)

        await async_step(self.page, f"Perform search for '{search_value}' and open GitHub repo", action, self.request)


