from playwright.sync_api import Page, Locator, expect

from ui.pages.base_page import BasePage


class CheckoutComplete(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.checkout_complete_url = f"{base_url}checkout-complete.html"
        self.complete_text: Locator = page.get_by_text("Thank you for your order!")

    def check_checkout_complete_page(self):
        expect(self.page).to_have_url(self.checkout_complete_url)

    def open_checkout_complete_page(self):
        self.page.goto(self.checkout_complete_url)
        self.check_checkout_complete_page()