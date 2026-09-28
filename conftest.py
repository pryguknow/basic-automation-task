import pytest
import requests
import logging
from playwright.sync_api import sync_playwright


BASE_URL = "https://reqres.in"
TEST_PAGE = "https://the-internet.herokuapp.com/login"
YOUR_TOKEN =  "your_api_token" ## setup your token (It is usually defined in the global env)



logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="session")
def context_url():
    logging.info(f"Context URL has been initialized '{BASE_URL}'")
    yield BASE_URL

@pytest.fixture(scope="session")
def api_session(context_url):
    current_session = requests.Session()

    current_session.headers.update({
        "Accept": "application/json",
        "x-api-key": YOUR_TOKEN
    })

    logging.info("SETUP: Creating API session")

    yield context_url, current_session

    logging.info("TEARDOWN: Closing API session")
    current_session.close()


@pytest.fixture(scope="session")
def browser_context():
    browser = sync_playwright().start().chromium.launch(headless=False)
    logging.info("Browser has been created")
    context = browser.new_context()

    yield context

    browser.close()
    logging.info("\nBrowser has been closed")

@pytest.fixture(scope="function")
def open_test_page(browser_context):

    page = browser_context.new_page()

    logging.info(f"Page {TEST_PAGE} has been created")

    page.goto(TEST_PAGE)
    page.wait_for_load_state("domcontentloaded")

    logging.info(f"Page {TEST_PAGE} has been loaded")

    yield page

    page.close()
    logging.info(f"\nPage {TEST_PAGE} has been closed")



