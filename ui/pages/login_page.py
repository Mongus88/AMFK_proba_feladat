from playwright.sync_api import Page, Locator, expect

from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.login_url = base_url
        self.username_input: Locator = page.get_by_role("textbox", name="Username")
        self.password_input: Locator = page.get_by_placeholder("Password")
        self.login_button: Locator = page.get_by_role("button", name="Login")

    def check_login(self):
        expect(self.page).to_have_url(self.login_url)

    def open_login(self):
        self.page.goto(self.login_url)
        self.check_login()

    def fill_username(self, keyword):
        self.username_input.fill(keyword)

    def fill_password(self, keyword):
        self.password_input.fill(keyword)

    def click_login_button(self):
        self.login_button.click()

    def full_login(self,username,password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()