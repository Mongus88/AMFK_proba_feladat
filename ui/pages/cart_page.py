from playwright.sync_api import Page, Locator, expect

from ui.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.cart_url = f"{base_url}cart.html"
        self.item_name: Locator = page.get_by_text("Sauce Labs Backpack")
        self.checkout_button: Locator = page.get_by_role("button", name="Checkout")

    def check_cart(self):
        expect(self.page).to_have_url(self.cart_url)

    def open_cart(self):
        self.page.goto(self.cart_url)
        self.check_cart()

    def click_checkout_button(self):
        self.checkout_button.click()