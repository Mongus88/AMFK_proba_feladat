from playwright.sync_api import expect

from ui.pages.inventory_page import InventoryPage
from ui.pages.cart_page import CartPage
from ui.pages.checkout_your_inf_page import CheckoutYourInfPage
from ui.pages.checkout_overview_page import CheckoutOverview
from ui.pages.checkout_complete_page import CheckoutComplete


def test_TC04_checkout_complete(logged_in_page, base_url):
    inventory_page = InventoryPage(logged_in_page, base_url)
    cart_page = CartPage(logged_in_page, base_url)
    checkout_page = CheckoutYourInfPage(logged_in_page, base_url)
    checkout_overview_page = CheckoutOverview(logged_in_page, base_url)
    checkout_complete_page = CheckoutComplete(logged_in_page, base_url)

    inventory_page.open_inventory()
    inventory_page.click_sauce_labs_backpack_add_to_cart()
    inventory_page.click_cart_icon()
    cart_page.click_checkout_button()
    checkout_page.fill_first_name("test1")
    checkout_page.fill_last_name("test2")
    checkout_page.fill_postal_code("5600")
    checkout_page.click_continue_button()
    checkout_overview_page.click_finish_button()

    expect(checkout_complete_page.complete_text).to_be_visible()
    expect(checkout_complete_page.complete_text).to_have_text("Thank you for your order!")