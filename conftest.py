import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):

    chrome_options = Options()

    # Detect GitHub Actions (CI)
    is_ci = os.getenv("GITHUB_ACTIONS") == "true"

    if is_ci:
        # ✅ GitHub Actions → headless mode
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        # ✅ Correct Chrome binary path
        chrome_options.binary_location = "/usr/bin/google-chrome"

    else:
        # ✅ Local → visible browser
        chrome_options.add_argument("--start-maximized")

    # ✅ Let Selenium auto-manage driver
    driver = webdriver.Chrome(options=chrome_options)

    # ✅ Open URL
    driver.get("https://mvp.intoleads.ai/login")
    driver.implicitly_wait(5)

    # Attach driver to class
    request.cls.driver = driver

    print("Automation started")

    yield

    # Teardown
    driver.quit()
    print("Automation finished")