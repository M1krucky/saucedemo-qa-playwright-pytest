from pages.inventory_page import InventoryPage
from pages.product_details_page import ProductDetailsPage


def test_open_product_and_back_to_inventory(page, login):
    """Verify a user can open a product details page and return to inventory."""
    login()  # authenticate user using reusable login fixture

    inventory = InventoryPage(page)  # inventory page object creation
    inventory.assert_loaded()  # confirm inventory page is displayed

    product_name = inventory.open_first_product()  # open first product and store its name for validation

    details = ProductDetailsPage(page)  # product details page object creation
    details.assert_loaded()  # confirm product details page is displayed
    details.assert_name(product_name)  # verify opened product matches selected inventory item
    details.assert_price_visible()  # confirm product price is displayed

    details.go_back_to_inventory()  # navigate back to inventory page
    inventory.assert_loaded()  # confirm inventory page is displayed again
