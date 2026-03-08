import pytest

from pages.login_page import LoginPage
from config import BASE_URL, USERNAME, PASSWORD


@pytest.mark.parametrize(
    "username,password,error_text",
    [  # parameter sets: (username, password, expected_error_message)
        ("", "", "Username is required"),
        ("locked_out_user", PASSWORD, "locked out"),
        (USERNAME, "wrong_password", "Username and password do not match"),
    ],
)
def test_login_negative_scenarios_show_error(page, username, password, error_text):
    """Verify login fails and an appropriate error message is shown for invalid credentials."""
    login_page = LoginPage(page)  # login page object creation

    login_page.open(BASE_URL)  # open login page
    login_page.assert_loaded()  # confirm login page is displayed

    if username == "" and password == "":
        login_page.submit()  # attempt login with empty credentials
    else:
        login_page.login_with(username, password)  # attempt login with invalid credentials

    login_page.assert_loaded()  # verify user remains on login page
    login_page.assert_error_contains(error_text)  # confirm expected error message is shown