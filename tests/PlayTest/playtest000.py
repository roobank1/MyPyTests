from playwright.sync_api import sync_playwright

from utils.steps import step

def test_has_title(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        step(page, "Open Playwright home page", lambda: page.goto("https://playwright.dev/"), request)

        def verify_title():
            assert "Playwright" in page.title()

        step(page, "Verify page title contains Playwright", verify_title, request)

        browser.close()

def test_get_started_link(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        step(page, "Open Playwright home page", lambda: page.goto("https://playwright.dev/"), request)

        step(page, "Click Get started link", lambda: page.get_by_role("link", name="Get started").click(), request)

        def verify_installation_heading():
            heading = page.get_by_role("heading", name="Installation")
            heading.wait_for(state="visible")
            assert heading.is_visible()

        step(page, "Verify Installation heading is visible", verify_installation_heading, request)

        browser.close()