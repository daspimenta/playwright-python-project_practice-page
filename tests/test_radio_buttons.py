from playwright.sync_api import Page, expect
import time


def test_click_radio_button(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")
    radio_a = page.get_by_role("radio", name="Option A")
    radio_a.click()
    expect(radio_a).to_be_checked
    radio_b = page.get_by_role("radio", name="Option B")
    radio_b.click()
    expect(radio_b).to_be_checked
