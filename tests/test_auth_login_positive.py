from pages.inventory_page import InventoryPage


def test_login_positive(page, login):
    """Verify a user can successfully log in and access the inventory page."""
    login()  # authenticate user using reusable login fixture

    inventory = InventoryPage(page)  # inventory page object creation
    inventory.assert_loaded()  # confirm inventory page is displayed
    inventory.assert_has_items(min_count=1)  # verify products are visible after login