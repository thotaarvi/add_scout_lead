import time

from Pages.add_leadpage import Addlead
from Pages.login_page import LoginPage
from config.config import BASE_URL, USERNAME, PASSWORD
import pygsheets
from datetime import datetime
import os
import base64


def get_leads_data():
    creds_base64 = os.getenv("GOOGLE_CREDS")

    if not creds_base64:
        raise Exception("GOOGLE_CREDS environment variable not set")

    # Create JSON file dynamically
    file_path = "service_account.json"

    with open(file_path, "w") as f:
        f.write(base64.b64decode(creds_base64).decode("utf-8"))

    # Authorize
    gc = pygsheets.authorize(service_account_file=file_path)

    sh = gc.open("Leadaddsheet2")
    worksheet = sh.sheet1

    data = worksheet.get_all_records()
    return worksheet,data


def test_valid_login(setup):
    driver = setup
    driver.get(BASE_URL)

    # Login
    login = LoginPage(driver)
    login.enter_username(USERNAME)
    login.enter_password(PASSWORD)
    login.click_login()

    # Navigate
    leads = Addlead(driver)
    leads.click_leads()

    # Fetch data
    worksheet, data = get_leads_data()

    for index, row in enumerate(data, start=2):
        try:
            leads.click_addleads_button()

            leads.enter_firstname(row.get("firstname", ""))
            leads.enter_lastname(row.get("lastname", ""))
            leads.enter_companyname(row.get("company", ""))
            leads.enter_emailname(row.get("email", ""))
            leads.enter_websitename(row.get("website", ""))

            leads.click_addlead()
            leads.scout_lead()
            leads.wait_for_toast()
            time.sleep(5)
            status = "PASS"

        except Exception as e:
            status = "FAIL"
            print(f"Error: {e}")


        exec_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        worksheet.update_value(f"F{index}", status)
        worksheet.update_value(f"G{index}", exec_time)