from playwright.sync_api import Page, expect


def test_all_locators(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

# get_by_role    
    expect(page.get_by_role("button", name="Explicit Role Button")).to_be_visible()
    expect(page.get_by_role("link", name="Explicit Role Link")).to_be_visible()    
    expect(page.get_by_role("img", name="robot icon")).to_be_visible()    
    expect(page.get_by_role("button", name="Implicit Button")).to_be_visible()    
    expect(page.get_by_role("link", name="Implicit Link")).to_be_visible()
    
# get_by_text
    expect(page.get_by_text("Locate elements by their visible text content.")).to_be_visible()
    expect(page.get_by_text("Playwright locator: get_by_text()")).to_be_visible()
    expect(page.get_by_text("This text span can be located by its text.")).to_be_visible()
    expect(page.get_by_text("Blue Box")).to_be_visible()
    expect(page.get_by_text("Locate form controls by their associated label text.")).to_be_visible()

# get_by_label
    expect(page.get_by_label("Email Address")).to_be_visible()
    page.get_by_label("Email Address").click()   
    expect(page.get_by_label("Accept Terms and Conditions")).to_be_visible()
    page.get_by_label("Accept Terms and Conditions").click()

# get_by_placeholder
    page.get_by_placeholder("Search for items...").click()
    page.get_by_placeholder("Enter your password").click()



