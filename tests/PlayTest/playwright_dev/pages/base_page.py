from utils.steps import async_step


class BasePage:
    def __init__(self, page, request):
        self.page = page
        self.request = request

    async def goto(self, url: str, step_name: str = "Open page"):
        async def action():
            await self.page.goto(url)

        await async_step(self.page, step_name, action, self.request)
