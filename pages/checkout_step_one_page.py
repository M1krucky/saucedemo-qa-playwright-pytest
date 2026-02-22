import re
from playwright.sync_api import Page, expect


class CheckoutStepOnePage:
    """
    SauceDemo Checkout - Step One Page object.

    Responsibilities:
    - Represents the customer information step of the checkout process.
    - Handles entering buyer details required to proceed with checkout.
    - Provides assertions confirming correct navigation to this step.
    """

    def __init__(self, page: Page):
        self.page = page  # Playwright browser tab used by this page object

        # Checkout form locators
        self.first_name = page.locator('[data-test="firstName"]')  # first name input field
        self.last_name = page.locator('[data-test="lastName"]')  # last name input field
        self.postal_code = page.locator('[data-test="postalCode"]')  # postal/ZIP code input field
        self.continue_button = page.locator('[data-test="continue"]')  # proceed to checkout overview

    # Assertions
    def assert_loaded(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/checkout-step-one\.html$"))  # confirm step one page is opened

    # Actions
    def fill_customer_info(self, first: str, last: str, postal: str) -> None:
        self.first_name.fill(first)  # enter customer's first name
        self.last_name.fill(last)  # enter customer's last name
        self.postal_code.fill(postal)  # enter postal code

    def continue_to_overview(self) -> None:
        self.continue_button.click()  # proceed to checkout overview (step two)