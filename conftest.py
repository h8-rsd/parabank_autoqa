import pytest

from playwright.sync_api import sync_playwright
from src.utils.step_reporter import StepReporter


# fixture == session
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


# fixture == function
@pytest.fixture(scope="function")
def report() -> StepReporter:
    return StepReporter()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    return page
