# SauceDemo QA Automation Project (Playwright + Pytest)

![CI](https://github.com/M1krucky/saucedemo-qa-playwright-pytest/actions/workflows/ci.yml/badge.svg)

UI test automation project built to demonstrate practical QA Automation skills and production-style test architecture.
The project demonstrates real-world test structure using Python, Pytest, Playwright, and Page Object Model (POM).

The automated tests target the public demo e-commerce application: https://www.saucedemo.com/

---

## Why this project

This project was created to demonstrate practical QA Automation skills and engineering-level test architecture.  
The focus is not only on writing tests, but on building a maintainable automation framework similar to real production QA environments.

---

## Tech Stack

- Python
- Pytest
- Playwright (sync API)
- Playwright Pytest plugin
- Page Object Model (POM)
- GitHub (CI planned)

---

## Project Goal

Build a job-level UI automation framework demonstrating:

- clean test architecture
- reusable fixtures
- Page Object Model design
- stable UI testing practices

---

## Current Test Coverage

### Authentication

- Positive login
- Wrong password
- Empty fields validation
- Locked user

### Inventory

- Inventory page loads
- Product details navigation

### Cart

- Add item
- Remove item

### Checkout

- Happy path checkout

### Security

- Logout
- Access restriction after logout

---

## Project Structure

```
saucedemo-qa-playwright-pytest/
│
├── pages/                # Page Object Model classes (UI interactions)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── product_details_page.py
│   ├── cart_page.py
│   ├── checkout_step_one_page.py
│   ├── checkout_step_two_page.py
│   └── checkout_complete_page.py
│
├── tests/                # Test suite
│   ├── conftest.py       # shared fixtures (browser setup, login fixture)
│   └── test_*.py         # UI test scenarios
│
├── config.py             # centralized configuration
├── pytest.ini            # pytest configuration
├── requirements.txt      # project dependencies
└── README.md
```

---

## Architecture Highlights

- Centralized configuration (`config.py`)
- Callable login fixture (explicit control of authentication)
- Full Page Object Model implementation
- Tests describe behaviour, page objects handle UI mechanics

---

## Test Scope

The test suite validates core user flows of the SauceDemo application:

- Authentication and access control
- Product browsing and navigation
- Cart management
- Checkout process
- Session security (logout and protected routes)

Tests focus on behaviour validation while UI interaction logic is encapsulated inside Page Objects.

---

## Project Status

UI automation framework completed with full Page Object Model implementation.
All tests are passing locally. CI integration planned next.

---

## Next Steps

- Add GitHub Actions CI
- Extend test coverage
- Introduce API + UI end-to-end validation

---

## How to Run Tests Locally

Clone the repository:

```bash
git clone https://github.com/M1krucky/saucedemo-qa-playwright-pytest.git
cd saucedemo-qa-playwright-pytest
```

Create virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows (Git Bash)
pip install -r requirements.txt
playwright install
```

Run tests:

```bash
pytest
```

---
