"""
Centralized test configuration.

Loads environment-specific settings for the SauceDemo application.
Environment variables allow overriding default values for CI or local runs.
"""

import os

BASE_URL = os.getenv("SAUCE_BASE_URL", "https://www.saucedemo.com/")
USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")


