from playwright.sync_api import Page, Locator, expect

from ui.pages.base_page import BasePage


class CheckoutOverview(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.checkout_overview_url = f"{base_url}checkout-step-two.html"
        self.sauce_labs_backpack_item: Locator = page.get_by_text("Sauce Labs Backpack")
        self.finish_button: Locator = page.get_by_role("button", name="finish")

    def check_checkout_overview_page(self):
        expect(self.page).to_have_url(self.checkout_overview_url)

    def open_checkout_overview_page(self):
        self.page.goto(self.checkout_overview_url)
        self.check_checkout_overview_page()

    def click_finish_button(self):
        self.finish_button.click()