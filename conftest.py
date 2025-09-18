import pytest
from typing import Generator
from playwright.sync_api import sync_playwright, Browser, Page

@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    """
    Launches a Chromium browser for the entire test session.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser) -> Generator[Page, None, None]:
    """
    Creates a new browser page for each test function.
    """
    page = browser.new_page()
    yield page
    page.close()
