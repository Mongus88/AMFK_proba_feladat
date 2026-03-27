import sys
import os
import pytest
from playwright.sync_api import Page

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.pages.login_page import LoginPage


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture
def logged_in_page(page: Page, base_url: str):
    login_page = LoginPage(page, base_url)
    login_page.open_login()
    login_page.full_login("standard_user", "secret_sauce")
    page.wait_for_url(f"{base_url}inventory.html")
    return page