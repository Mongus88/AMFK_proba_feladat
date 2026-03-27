from playwright.sync_api import Page, Locator, expect

from ui.pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.inventory_url = f"{base_url}inventory.html"
        self.sauce_labs_backpack_add_to_cart: Locator = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_icon: Locator = page.locator("[data-test='shopping-cart-link']")

    def check_inventory(self):
        expect(self.page).to_have_url(self.inventory_url)

    def open_inventory(self):
        self.page.goto(self.inventory_url)
        self.check_inventory()

    def click_sauce_labs_backpack_add_to_cart(self):
        self.sauce_labs_backpack_add_to_cart.click()

    def click_cart_icon(self):
        self.cart_icon.click()