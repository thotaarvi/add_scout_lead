from selenium import webdriver
import pytest
import time

@pytest.fixture
def setup():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    time.sleep(5)

    driver.quit()