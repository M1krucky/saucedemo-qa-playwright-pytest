from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_logout_and_inventory_not_accessible_after_logout(page, login):
    """Verify user is logged out and inventory page cannot be accessed after logout."""
    login()  # authenticate user using reusable login fixture

    inventory = InventoryPage(page)  # inventory page object creation
    inventory.assert_loaded()  # confirm inventory page is displayed

    inventory.logout()  # perform logout via application menu

    login_page = LoginPage(page)  # login page object creation
    login_page.assert_loaded()  # confirm user is redirected to login page

    page.goto("https://www.saucedemo.com/inventory.html")  # attempt direct access to protected inventory page

    login_page.assert_loaded()  # verify access is denied and login page is displayed