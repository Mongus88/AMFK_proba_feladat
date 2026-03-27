from playwright.sync_api import expect

from ui.pages.login_page import LoginPage


def test_TC01_valid_login(page, base_url):
    login_page = LoginPage(page, base_url)
    login_page.open_login()
    login_page.fill_username("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()


    expect(page).to_have_url(f"{base_url}inventory.html")