from playwright.sync_api import expect

from ui.pages.inventory_page import InventoryPage
from ui.pages.cart_page import CartPage


def test_TC02_cart_chech(logged_in_page, base_url):
    inventory_page = InventoryPage(logged_in_page, base_url)
    cart_page = CartPage(logged_in_page, base_url)

    inventory_page.open_inventory()
    inventory_page.click_sauce_labs_backpack_add_to_cart()
    inventory_page.click_cart_icon()

    expect(cart_page.item_name).to_be_visible()
    expect(cart_page.item_name).to_have_text("Sauce Labs Backpack")
