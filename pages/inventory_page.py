from playwright.sync_api import Page, expect


class InventoryPage:
    """
    SauceDemo Inventory Page object.

    Responsibilities:
    - Represents the product inventory (catalog) screen after successful login.
    - Provides interactions with products, cart actions, and main navigation controls.
    - Contains assertions verifying inventory visibility and cart state.
    """

    def __init__(self, page: Page):
        self.page = page  # Playwright browser tab used by this page object

        # Inventory locators
        self.title = page.locator('[data-test="title"]')  # page title ("Products")
        self.items = page.locator('[data-test="inventory-item-name"]')  # all product names in inventory list
        self.first_item_name = self.items.first  # first product in inventory (used for navigation tests)

        # Cart locators
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')  # cart item count badge
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')  # cart icon/link in header

        # Navigation / menu locators
        self.menu_button = page.get_by_role("button", name="Open Menu")  # burger menu button
        self.logout_link = page.locator('[data-test="logout-sidebar-link"]')  # logout link inside side menu

    # Assertions
    def assert_loaded(self) -> None:
        expect(self.title).to_have_text("Products")  # confirms inventory page is displayed

    def assert_has_items(self, min_count: int = 1) -> None:
        expect(self.items.first).to_be_visible()  # at least one product is visible

    def assert_cart_badge(self, expected_count: int) -> None:
        expect(self.cart_badge).to_have_text(str(expected_count))  # verify cart item count

    def assert_cart_badge_hidden(self) -> None:
        expect(self.cart_badge).to_have_count(0)  # badge disappears when cart becomes empty

    # Actions
    def open_first_product(self) -> str:
        name_text = self.first_item_name.inner_text()  # capture product name before navigation
        self.first_item_name.click()  # open product details page
        return name_text  # return name for later validation on details page

    def add_item_to_cart(self, item_slug: str) -> None:
        self.page.locator(f'[data-test="add-to-cart-{item_slug}"]').click()  # add specific product to cart

    def open_cart(self) -> None:
        self.cart_link.click()  # navigate to cart page

    def logout(self) -> None:
        self.menu_button.click()  # open side menu
        expect(self.logout_link).to_be_visible()  # wait until menu animation completes
        self.logout_link.click()  # perform logout


 