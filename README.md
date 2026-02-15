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

In progress — Page Object Model migration and CI integration.

---

## Next Steps

- Complete Page Object Model refactor
- Add GitHub Actions CI
- Improve test parametrization
