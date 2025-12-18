from playwright.sync_api import sync_playwright
import re

def run_sync_automation():
    # 1. Start Playwright in the synchronous context manager
    # This handles the setup and teardown automatically.
    with sync_playwright() as p:
        
        # 2. Launch the Chromium browser
        # Note: We use .launch() without 'await' in the synchronous context.
        browser = p.chromium.launch(headless=False) 
        
        # 3. Create a new browser page (tab)
        page = browser.new_page()

        # 4. Navigate to the target URL
        
        page.goto("https://app.fivesurveys.com/surveys")

        # 5. Get and print the page title
        page_title = page.title()
        print(f"Page Title: **{page_title}**")
        # Use the attribute selector directly
        # Use the attribute selector directly
        email_selector = 'input[data-test-id="app-page-email-field-input"]'

        # Wait for it to be attached to the page first
        page.wait_for_selector(email_selector, state="attached")

        # Fill it
        page.locator(email_selector).fill("Jimmyjimmyjonjon1@gmail.com")
        page.locator('button[data-test-id="app-page-continue-button"]').click()
        page.locator('input[data-test-id="undefined-input"]').fill("Jimmyjonpass1!")
        page.get_by_text("Continue").click()
        page.locator('label[data-test-id="ps-offers-platforms-popup-desktop-label-desktop"]').click()
        page.get_by_text("Save Selection").click()
        page.locator(".list-item").first.wait_for()
        for i in page.locator(".five-survey-tile").all():
            print(i.inner_text())
        



        
        input()

if __name__ == "__main__":
    run_sync_automation()