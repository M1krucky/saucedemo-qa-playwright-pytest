import re
from playwright.sync_api import Page, expect


class CheckoutStepTwoPage:
    """
    SauceDemo Checkout - Step Two (Overview) Page object.

    Responsibilities:
    - Represents the checkout overview step where the user reviews the order.
    - Provides verification that the overview page is displayed.
    - Handles completion of the checkout process.
    """

    def __init__(self, page: Page):
        self.page = page  # Playwright browser tab used by this page object

        # Checkout overview locators
        self.finish_button = page.locator('[data-test="finish"]')  # finish checkout button

    # Assertions
    def assert_loaded(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/checkout-step-two\.html$"))  # confirm overview page is opened

    # Actions
    def finish(self) -> None:
        self.finish_button.click()  # complete checkout and navigate to confirmation page