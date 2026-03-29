import { test, expect } from '@playwright/test';

// Test function for Playwright tests

test('Playwright Example', async ({ page }) => {
    // Ensure the browser always closes
    await page.goto('https://example.com');
    await page.click('text=More information...');
    // Add additional navigation/click steps here
});
