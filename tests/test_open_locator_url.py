from playwright.sync_api import Page, expect


def test_all_locators(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")
    pwlocator_button = page.get_by_role("button", name="Test Playwright Locators")
    pwlocator_button.click()
