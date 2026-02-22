from pages.login_page import LoginPage
from config import BASE_URL, PASSWORD


def test_login_locked_user_shows_error(page):
    """Verify login fails and an error is shown for a locked user account."""
    login_page = LoginPage(page)  # login page object creation

    login_page.open(BASE_URL)  # open login page
    login_page.assert_loaded()  # confirm login page is displayed

    login_page.login_with("locked_out_user", PASSWORD)  # attempt login with locked account

    login_page.assert_loaded()  # verify user remains on login page
    login_page.assert_error_contains("locked out")  # confirm locked user error message is shown