import os

BASE_URL = os.getenv("SAUCE_BASE_URL", "https://www.saucedemo.com/")
USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")

# 👉 Yes. "SAUCE_BASE_URL"/ "SAUCE_USERNAME"/ "SAUCE_PASSWORD" can be any name.
# You invented it. Python doesn’t care.

# It looks for an environment variable
# named "SAUCE_BASE_URL"/ "SAUCE_USERNAME"/ "SAUCE_PASSWORD"
# If it exists → use its value
# If not → use default
# Python does not define "SAUCE_BASE_URL" anywhere.
# It’s just a string key.

