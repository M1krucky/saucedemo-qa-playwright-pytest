import re
from playwright.sync_api import Page, expect


class CheckoutCompletePage:
    """
    SauceDemo Checkout Complete Page object.

    Responsibilities:
    - Represents the final confirmation screen after successful checkout.
    - Provides verification that checkout completed successfully.
    """

    def __init__(self, page: Page):
        self.page = page  # Playwright browser tab used by this page object

        # Confirmation page locators
        self.complete_header = page.locator('[data-test="complete-header"]')  # success confirmation message

    # Assertions
    def assert_loaded(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/checkout-complete\.html$"))  # confirm confirmation page is opened

    def assert_success_message(self) -> None:
        expect(self.complete_header).to_have_text("Thank you for your order!")  # verify successful checkout message