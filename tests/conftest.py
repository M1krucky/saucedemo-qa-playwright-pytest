import re
import pytest
import os  # filesystem operations for artifacts output
from playwright.sync_api import expect
from config import BASE_URL, USERNAME, PASSWORD
from datetime import datetime  # timestamp naming for screenshot files 


@pytest.fixture # @pytest.fixture registers login as a pytest fixture.
def login(page): # Page is injected by pytest-playwright.
    """
    Returns a callable that logs in using config credentials.
    Usage in tests: login()
    """
    def _login():
        page.goto(BASE_URL)
        page.locator('[data-test="username"]').fill(USERNAME)
        page.locator('[data-test="password"]').fill(PASSWORD)
        page.locator('[data-test="login-button"]').click()
        expect(page).to_have_url(re.compile(r".*/inventory\.html$"))

    return _login # returns the function object (function itself)

 
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a Playwright screenshot on test failure during execution phase."""
    outcome = yield  # execute test and obtain result
    report = outcome.get_result()  # retrieve execution report object

    if report.when != "call":  # capture only during test execution phase
        return

    if report.passed:  # no artifact needed for successful tests
        return

    page = item.funcargs.get("page")  # access Playwright page fixture if available
    if page is None:  # skip non-UI tests
        return

    os.makedirs("artifacts/screenshots", exist_ok=True)  # ensure artifact directory exists
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # generate unique timestamp
    safe_test_name = item.nodeid.replace("/", "_").replace("::", "__")  # normalize test identifier for filesystem
    file_path = f"artifacts/screenshots/{safe_test_name}_{timestamp}.png"  # construct screenshot path

    page.screenshot(path=file_path, full_page=True)  # capture full-page screenshot for failure diagnostics