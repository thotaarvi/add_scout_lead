from Pages.add_leadpage import Addlead
from Pages.login_page import LoginPage
from config.config import BASE_URL, USERNAME, PASSWORD
import pygsheets
import time
import os
import base64
import json


def get_leads_data():

    creds_base64 = os.getenv("GOOGLE_CREDS")

    if not creds_base64:
        raise Exception("GOOGLE_CREDS environment variable not set")

    creds_json = base64.b64decode(creds_base64).decode("utf-8")
    creds_dict = json.loads(creds_json)

    gc = pygsheets.authorize(service_account_json=creds_dict)

    sh = gc.open("Leadaddsheet2")
    worksheet = sh.sheet1

    return worksheet.get_all_records()


def test_valid_login(setup):

    driver = setup
    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.enter_username(USERNAME)
    login.enter_password(PASSWORD)
    login.click_login()

    leads = Addlead(driver)

    leads.click_leads()


    data = get_leads_data()



    for row in data:
        leads.click_addleads_button()

        leads.enter_firstname(row["firstname"])
        leads.enter_lastname(row["lastname"])
        leads.enter_companyname(row["company"])
        leads.enter_emailname(row["email"])
        leads.enter_websitename(row["website"])

        leads.click_addlead()
        time.sleep(3)

        leads.scout_lead()
        leads.wait_for_toast()

        time.sleep(5)