from pages.inventory_page import InventoryPage


def test_inventory_page_loads(page, login):
    """Verify inventory page loads successfully and displays available products."""
    login()  # authenticate user using reusable login fixture

    inventory = InventoryPage(page)  # inventory page object creation
    inventory.assert_loaded()  # confirm inventory page is displayed
    inventory.assert_has_items(min_count=1)  # verify products are visible on inventory page

    