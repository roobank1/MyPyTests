from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False , slow_mo=300)
    page = browser.new_page()
    page.goto("https://dotesthere.com")
    # Add a brief wait to ensure the page loads
    # page.wait_for_load_state("networkidle")
    
    Test_Link1 = page.get_by_role("banner").get_by_role("link", name="API Testing")
    Test_Link2 = page.get_by_role("banner").get_by_role("link", name="Web Elements")
    Test_Link2_1 = page.get_by_role("link", name="A/B Testing")
    Test_Link2_2 = page.get_by_role("link", name="Add/Remove Elements")
    Test_Link3 = page.get_by_role("banner").get_by_role("link", name="Manual Testing Lab")


    Test_Link1.click()
    page.wait_for_timeout(1000)
    
    Test_Link2.click()
    page.wait_for_timeout(1000)
    Test_Link2_1.click()
    page.wait_for_timeout(1000)
    Test_Link2_2.click()
    page.wait_for_timeout(1000)
    
    Test_Link3.click()
    page.wait_for_timeout(1000)


        
    # Close the browser to free resources
    browser.close()    