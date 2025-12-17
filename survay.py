from playwright.sync_api import sync_playwright

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
        
        page.goto("https://www.chess.com/home")

        # 5. Get and print the page title
        page_title = page.title()
        print(f"Page Title: **{page_title}**")

        # 6. Perform a simple action (e.g., take a screenshot)
        page.locator("#login-username").fill("balls")
        input()
        # 7. Close the browser
        browser.close()
        print("\nAutomation complete. Browser closed.")

if __name__ == "__main__":
    run_sync_automation()