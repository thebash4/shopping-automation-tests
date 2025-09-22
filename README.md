🧪 Pytest + Playwright Automation Framework

This project is an automated testing suite for a shopping web application, built with Playwright for browser automation and Pytest for test execution and reporting.

✨ Features

End-to-End UI Tests: Validates key user flows including homepage navigation, product listing, add-to-cart, and checkout.

Cross-Browser Support: Runs tests on Chromium, Firefox, and WebKit.

HTML Reporting: Generates detailed, timestamped HTML reports for each run.

CI/CD Ready: Easily integrates with GitHub Actions (or any CI/CD pipeline) for automated testing on every commit or pull request.

⚡ Prerequisites

Python 3.8+

Node.js
 (for Playwright browser binaries)

Git

🚀 Setup & Installation

Clone the Repository

git clone <your-repo-url>
cd <your-project-folder>


Create & Activate a Virtual Environment

python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install Python Dependencies

pip install -r requirements.txt


Install Playwright Browsers

playwright install

🧑‍💻 Running Tests

Run All Tests

pytest


Run with HTML Report

pytest --html=reports/report.html


Run Specific Test File

pytest tests/test_cart.py


Run with Markers (e.g., smoke)

pytest -m smoke --html=reports/smoke_report.html

⚙️ CI/CD Integration

Add a GitHub Actions workflow (or your CI provider) to:

Install dependencies

Run pytest

Upload the HTML report as an artifact

📂 Project Structure
├─ tests/               # Test cases (Pytest)
├─ pages/               # Page Object Models
├─ reports/             # HTML reports output
├─ requirements.txt     # Python dependencies
└─ pytest.ini           # Pytest configuration
