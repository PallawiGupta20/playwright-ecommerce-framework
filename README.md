# Playwright E-Commerce Test Automation Framework

A Page Object Model (POM) based web UI test automation framework built with 
Playwright, Python, and pytest, tested against saucedemo.com.

## Tech Stack
- Python 3
- Playwright (Chromium/Firefox/WebKit)
- pytest + pytest-playwright
- Page Object Model design pattern
- Allure reporting

## Project Structure

## Setup
```bash
git clone https://github.com/PallawiGupta20/playwright-ecommerce-framework.git
cd playwright-ecommerce-framework
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Running Tests
```bash
pytest -v                          # headless
pytest --headed -v                 # see the browser
pytest --browser firefox -v        # run on Firefox instead of Chromium
```

## What This Project Demonstrates
- Page Object Model applied to web UI testing
- Data-driven login testing (valid/invalid/locked-out users)
- Full end-to-end purchase flow (login -> cart -> checkout -> confirmation)
- Reusable pytest fixtures for page setup
- CI/CD integration via GitHub Actions
