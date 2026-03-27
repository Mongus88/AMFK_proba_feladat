from playwright.sync_api import Page, Locator, expect

from ui.pages.base_page import BasePage


class CheckoutYourInfPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.checkout_your_inf_page_url = f"{base_url}checkout-step-one.html"
        self.first_name_input: Locator = page.get_by_role("textbox", name="First Name")
        self.last_name_input: Locator = page.get_by_role("textbox", name="Last Name")
        self.postal_code_input: Locator = page.get_by_role("textbox", name="Zip/Postal Code")
        self.continue_button: Locator = page.get_by_role("button", name="continue")

    def check_checkout_your_inf_page(self):
        expect(self.page).to_have_url(self.checkout_your_inf_page_url)

    def open_checkout_your_inf_page(self):
        self.page.goto(self.checkout_your_inf_page_url)
        self.check_checkout_your_inf_page()

    def fill_first_name(self, keyword):
        self.first_name_input.fill(keyword)

    def fill_last_name(self, keyword):
        self.last_name_input.fill(keyword)

    def fill_postal_code(self, keyword):
        self.postal_code_input.fill(keyword)

    def click_continue_button(self):
        self.continue_button.click()