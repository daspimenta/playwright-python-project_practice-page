from playwright.sync_api import Page, expect
import time

def test_all_locators(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")
    pw_locator = page.get_by_role("button", name="Test Playwright Locators")
    pw_locator.click()
    
