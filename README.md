# SauceDemo QA Automation Project (Playwright + Pytest)

UI test automation project built as part of a QA Automation learning and portfolio journey.
The project demonstrates real-world test structure using Python, Pytest, Playwright, and Page Object Model (POM).

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

## Architecture Highlights

- Centralized configuration (`config.py`)
- Callable login fixture (explicit control of authentication)
- Incremental migration to Page Object Model
- Tests describe behaviour, page objects handle UI mechanics

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
