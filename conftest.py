from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def setup():
    chrome_options = Options()

    # Required for CI / Linux (GitHub Actions)
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Optional but useful
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)

    yield driver

    driver.quit()