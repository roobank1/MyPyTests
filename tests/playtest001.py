import os
from playwright.sync_api import sync_playwright

def test_playwright_navigation():
    # GitHub Actions sets CI=true; default to headless in CI
    headless = os.getenv("CI", "").lower() == "true" or os.getenv("HEADLESS", "1") == "1"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            slow_mo=300 if not headless else 0,
        )
        page = browser.new_page()
        page.goto("https://dotesthere.com")

        page.get_by_role("banner").get_by_role("link", name="API Testing").click()
        page.wait_for_timeout(1000)

        page.get_by_role("banner").get_by_role("link", name="Web Elements").click()
        page.wait_for_timeout(1000)

        page.get_by_role("link", name="A/B Testing").click()
        page.wait_for_timeout(1000)

        page.get_by_role("link", name="Add/Remove Elements").click()
        page.wait_for_timeout(1000)

        page.get_by_role("link", name="Add/Remove Elements").click()
        page.wait_for_timeout(1000)

        page.get_by_role("banner").get_by_role("link", name="Manual Testing Lab").click()
        page.wait_for_timeout(1000)

        browser.close()
