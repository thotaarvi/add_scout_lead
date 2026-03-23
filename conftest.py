from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time

@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/google-chrome"
    chrome_options.add_argument("--headless")  # IMPORTANT
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    time.sleep(5)

    driver.quit()