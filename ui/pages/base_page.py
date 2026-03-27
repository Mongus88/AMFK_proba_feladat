from playwright.sync_api import expect, Page


class BasePage:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url