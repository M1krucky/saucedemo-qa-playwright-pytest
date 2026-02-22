from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_item_to_cart_updates_badge_and_cart(page, login):
    """Verify adding an item updates the cart badge and the item appears in the cart."""
    login()  # authenticate user using reusable login fixture

    item_name = "Sauce Labs Backpack"  # stable product name used for cart verification
    item_slug = "sauce-labs-backpack"  # stable product identifier used by SauceDemo selectors

    inventory = InventoryPage(page)  # inventory page object creation
    inventory.assert_loaded()  # confirm inventory page is displayed

    inventory.add_item_to_cart(item_slug)  # add selected product to cart
    inventory.assert_cart_badge(expected_count=1)  # verify cart badge reflects added item

    inventory.open_cart()  # navigate to cart page

    cart = CartPage(page)  # cart page object creation
    cart.assert_loaded()  # confirm cart page is displayed
    cart.assert_item_present(item_name)  # verify selected item is present in cart