import sys
import os
from dotenv import load_dotenv
import pytest
from playwright.sync_api import Page

load_dotenv()

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.pages.login_page import LoginPage
from api.clients.users_client import ReqresClient


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture
def logged_in_page(page: Page, base_url: str):
    login_page = LoginPage(page, base_url)
    login_page.open_login()
    login_page.full_login(os.getenv("TEST_USER"), os.getenv("TEST_PASSWORD"))
    page.wait_for_url(f"{base_url}inventory.html")
    return page

# ----------- API -----------

@pytest.fixture(scope="session")
def api_base_url():
    return "https://reqres.in/api"


@pytest.fixture(scope="session")
def api_headers():
    api_key = os.getenv("X_API_KEY", os.getenv("API_TOKEN"))

    return {
        "x-api-key": api_key,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

@pytest.fixture(scope="session")
def reqres_client(api_request_context, api_base_url, api_headers):
    client = ReqresClient(
        api_request_context=api_request_context,
        base_url=api_base_url,
        headers=api_headers
    )
    return client

@pytest.fixture(scope="session")
def api_request_context(playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()
