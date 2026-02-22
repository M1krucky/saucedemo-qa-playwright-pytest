import re
from playwright.sync_api import Page, expect


class LoginPage:
    """
    SauceDemo Login Page object.

    Responsibilities:
    - Handles navigation to the login screen.
    - Handles login form interactions.
    - Provides assertions related to login state and validation errors.
    """

    def __init__(self, page: Page):
        self.page = page  # Playwright browser tab used by this page object

        # Login form locators
        self.username_input = page.locator('[data-test="username"]')  # username input field
        self.password_input = page.locator('[data-test="password"]')  # password input field
        self.login_button = page.locator('[data-test="login-button"]')  # login/submit button
        self.error = page.locator('[data-test="error"]')  # error banner displayed after failed login

    # Assertions
    def assert_loaded(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/$"))  # login page URL ends with "/"
        expect(self.login_button).to_be_visible()  # login form is visible and ready

    def assert_error_contains(self, text: str) -> None:
        expect(self.error).to_be_visible()  # error message must appear
        expect(self.error).to_contain_text(text)  # error text should contain expected message

    # Actions
    def open(self, base_url: str) -> None:
        self.page.goto(base_url)  # navigate to login page

    def submit(self) -> None:
        self.login_button.click()  # submit login form with current field values

    def login_with(self, username: str, password: str) -> None:
        self.username_input.fill(username)  # enter username
        self.password_input.fill(password)  # enter password
        self.submit()  # submit credentials