import re
from playwright.sync_api import Page, expect


class CartPage:
    """
    SauceDemo Cart Page object.

    Responsibilities:
    - Represents the shopping cart view.
    - Provides interactions for validating cart contents and removing items.
    - Handles navigation from cart to the checkout process.
    """

    def __init__(self, page: Page):
        self.page = page  # Playwright browser tab used by this page object

        # Cart locators
        self.cart_item_names = page.locator('[data-test="inventory-item-name"]')  # product names listed in cart
        self.remove_button_by_slug = lambda slug: page.locator(f'[data-test="remove-{slug}"]')  # dynamic remove button locator for a specific item
        self.checkout_button = page.locator('[data-test="checkout"]')  # button to start checkout

    # Assertions
    def assert_loaded(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/cart\.html$"))  # confirm cart page is opened

    def assert_item_present(self, expected_name: str) -> None:
        expect(self.cart_item_names.filter(has_text=expected_name).first).to_be_visible()  # verify item with given name exists in cart

    def assert_item_not_present(self, expected_name: str) -> None:
        expect(self.cart_item_names.filter(has_text=expected_name)).to_have_count(0)  # ensure item is no longer listed in cart

    # Actions
    def remove_item(self, item_slug: str) -> None:
        self.remove_button_by_slug(item_slug).click()  # remove specified item from cart

    def start_checkout(self) -> None:
        self.checkout_button.click()  # navigate to checkout step one

