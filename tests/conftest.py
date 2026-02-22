import re
import pytest
from playwright.sync_api import expect

from config import BASE_URL, USERNAME, PASSWORD


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

    return _login # returns the function object. Not the result of running it. Not the lines inside it. Just the function itself.
 

# What is "page" in def login(page)?
# page is a pytest fixture provided by pytest-playwright.
# You don’t create it.
# You don’t import it.
# You just ask for it by name in a function argument, and pytest injects it.
# So when pytest runs a test (or a fixture) that has page as an argument, it does roughly:
# start browser
# create a new context (clean state)
# open a new tab (that tab is page)
# pass that page object into your function
# after test finishes → close everything

# Why login and _login?
# We want two layers:
# A) login (outer) = fixture
# This is what pytest knows.
# Pytest sees: there is a fixture named login.
# So a test can request it:
# B) _login (inner) = function that does the action
# Inside the fixture we define:
# def _login():
# This _login() is the actual “do the login steps” action.

#3) Why define _login inside login?
# Because _login needs access to page, BASE_URL, USERNAME, PASSWORD.
# If _login is inside, it can “see” page from the outer function.
# This is called a closure.
# So _login() can use page without having to pass it every time.
# Think of it like:
#   outer function receives page
#   inner function uses that same page

# Why return _login?
# Because we want the test to be able to call it when it wants.
# If we wrote a fixture like this:
# @pytest.fixture
# def login(page):
#    page.goto(...)
# Then login would happen immediately whenever the fixture is requested.
# But sometimes you may want:
# a test that starts logged out, then logs in later
# a test that logs in twice
# a test that checks behavior before login
# So returning a callable is flexible.

# Who “returns it”? Where does it go?
# When a test requests the fixture:
# def test_inventory(login):
#    login()
# Pytest does:
#   1. run the fixture login(page)
#   2. fixture returns _login (a function object)
#   3. pytest gives that returned object to the test as the variable login
# So in the test:
#   * login is now the function _login
#   * calling login() runs the login steps
# This is why the naming is a bit confusing: fixture name login becomes a variable login inside the test, holding the returned callable.

# return _login returns:
# A function object that encapsulates the login steps and has access to page and config values via closure.
# It does NOT return the result of executing those steps.

#The precise difference:
# return _login:
#   * Return the function object.
#   * Test receives a callable.
# return _login():
#   * Execute the function immediately.
#   * Return its result (None).
#   * Test receives None.
# That is the entire trick.
# We return the function so that the test controls when login happens.

# Very precise breakdown:
# When Python sees:
# def _login():
#    page.goto(BASE_URL)
#    ...
# It creates a function object in memory.
# When you write:
# return _login
# You are returning a reference to that function object.
# The code inside it is stored, but not executed.

# ___________________________________________________________________________
# Let’s restate it in very precise terms so it becomes solid in your brain.

# Given:
# @pytest.fixture
# def login(page):
#    def _login():
#        page.goto(BASE_URL)
#        ...
#    return _login

# And test:

# def test_x(login):
    login()

# What happens step-by-step
# 1️⃣ def test_x(login):

# Pytest sees argument login.

# It does:
# Find fixture named login
# Execute that fixture function: login(page)
# Take what it returns
# Inject that return value into test as variable login

# So at this moment:

# Inside test:

# login == _login

# 2️⃣ login()

# Now you are calling the returned function object.

# So this executes _login().

# That runs:

# page.goto(...)
# fill username
# ...

# So yes — your sentence is correct:

# def test_x(login): -> this calls a fixture (outer function)
# login() -> this calls an inner function (object)

# More precisely:
# def test_x(login) → pytest executes the fixture
# login() → executes the function returned by the fixture
# Extremely important distinction
# The outer function:
# def login(page):
# is called automatically by pytest.
# The inner function:
# def _login():
# is called manually by you.
# That separation is intentional.

# Why this design is powerful
# It allows:

# def test_complex_flow(login):
#    # do something before login
#    login()
#    # do something after login
#    login()  # maybe re-login


# You control timing.

# You now understand:
# Fixture execution
# Function objects
# Closure
# Callable vs executed function
# Dependency injection
# That’s a real jump in understanding.