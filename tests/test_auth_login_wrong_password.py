from pages.login_page import LoginPage
from config import BASE_URL, USERNAME


def test_login_wrong_password_shows_error(page):
    """Verify login fails and an error message is shown when password is incorrect."""
    login_page = LoginPage(page)  # login page object creation

    login_page.open(BASE_URL)  # open login page
    login_page.assert_loaded()  # confirm login page is displayed

    login_page.login_with(USERNAME, "wrong_password")  # attempt login with invalid password

    login_page.assert_loaded()  # verify user remains on login page
    login_page.assert_error_contains("Username and password do not match")  # confirm correct error message is shown
