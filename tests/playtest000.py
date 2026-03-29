from playwright.sync_api import sync_playwright

def test_has_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playwright.dev/")

        # Expect a title "to contain" a substring.
        assert "Playwright" in page.title()

        browser.close()

def test_get_started_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playwright.dev/")

        # Click the get started link.
        page.get_by_role("link", name="Get started").click()

        # Wait for the heading to appear.
        heading = page.get_by_role("heading", name="Installation")
        heading.wait_for(state="visible")

        # Expects page to have a heading with the name of Installation.
        assert heading.is_visible()

        browser.close()