import re
from playwright.sync_api import Page, expect


class ProductDetailsPage:
    """
    SauceDemo Product Details Page object.

    Responsibilities:
    - Represents the product details view opened from the inventory page.
    - Provides assertions verifying correct product information is displayed.
    - Handles navigation back to the inventory list.
    """

    URL_PATH_PART = "/inventory-item.html"  # URL fragment identifying product details page

    def __init__(self, page: Page):
        self.page = page  # Playwright browser tab used by this page object

        # Product details locators
        self.name = page.locator('[data-test="inventory-item-name"]')  # product name on details page
        self.price = page.locator('[data-test="inventory-item-price"]')  # product price element
        self.back_to_products = page.locator('[data-test="back-to-products"]')  # button returning to inventory

    # Assertions
    def assert_loaded(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/inventory-item\.html.*"))  # confirm navigation to details page
        expect(self.name).to_be_visible()  # product content is visible

    def assert_name(self, expected_name: str) -> None:
        expect(self.name).to_have_text(expected_name)  # verify opened product matches selected item

    def assert_price_visible(self) -> None:
        expect(self.price).to_be_visible()  # ensure product price is displayed

    # Actions
    def go_back_to_inventory(self) -> None:
        self.back_to_products.click()  # navigate back to inventory page