from pages.login_page import LoginPage
from config import BASE_URL


def test_login_empty_fields_shows_error(page):
    """Verify login fails and a validation error is shown when credentials are empty."""
    login_page = LoginPage(page)  # login page object creation

    login_page.open(BASE_URL)  # open login page
    login_page.assert_loaded()  # confirm login page is displayed

    login_page.submit()  # attempt login with empty credentials

    login_page.assert_loaded()  # verify user remains on login page
    login_page.assert_error_contains("Username is required")  # confirm required-field error message is shown 