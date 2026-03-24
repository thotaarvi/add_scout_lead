from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




class Addlead:

    leads = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div/div[1]/div/div[2]/ul/li[1]/a")
    addLeads_button = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/main/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div/button")
    firstname = (By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/form/div[1]/div[2]/input")
    lastname = (By.XPATH,"/html/body/div[4]/div/div[2]/div[1]/form/div[1]/div[3]/input")
    companyname = (By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/form/div[1]/div[4]/input")
    emailname = (By.XPATH,"//html/body/div[4]/div/div[2]/div[1]/form/div[1]/div[5]/input")
    websitename = (By.XPATH,"/html/body/div[4]/div/div[2]/div[1]/form/div[1]/div[6]/input")
    addlead = (By.XPATH,"/html/body/div[4]/div/div[2]/div[1]/form/div[2]/button")
    #status =  (By.XPATH, "//button[contains(text(),'Scouting')]")

    def __init__(self, driver):
        self.driver = driver


    def click_leads(self):
        self.driver.find_element(*self.leads).click()
    def click_addleads_button(self):
        self.driver.find_element(*self.addLeads_button).click()
    def enter_firstname(self,firstname):
        self.driver.find_element(*self.firstname).send_keys(firstname)
    def enter_lastname(self,lastname):
        self.driver.find_element(*self.lastname).send_keys(lastname)
    def enter_companyname(self,companyname):
        self.driver.find_element(*self.companyname).send_keys(companyname)
    def enter_emailname(self,emailname):
        self.driver.find_element(*self.emailname).send_keys(emailname)
    def enter_websitename(self,websitename):
        self.driver.find_element(*self.websitename).send_keys(websitename)
    def click_addlead(self):
        self.driver.find_element(*self.addlead).click()

    def scout_lead(self):
        scout_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Scout')]")
        scout_btn.click()

    def wait_for_toast(self):
        wait = WebDriverWait(self.driver, 15)
        toast = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Scout Completed')]")))
        return toast.text