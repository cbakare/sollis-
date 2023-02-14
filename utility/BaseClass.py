import inspect
import logging
import time
import functools

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage



@pytest.mark.usefixtures("setup")

class BaseClass():
    def __init__(self, driver):
        self.driver = driver


    ScheduleAppLinkHome=(By.XPATH,"//p[text()='Schedule Appointment']")
    ScheduleAppPageHeader=(By.XPATH,"//h1[text()='Schedule Appointments']")

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))


    def HoldMouseArrowDown(self, Xpath):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"Xpath"))).send_keys(Keys.DOWN)

    def ScrollDowntoPage(self):
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def VerifyButtonChecked(self,text):
        self.driver.execute_script(f"return document.getElementById().checked")


    def signin(self,setup):
        WebDriverWait(self.driver,10).until(EC.title_contains("Member Portal"))
        self.driver.refresh()
        time.sleep(5)

    def Login(self,LoginpageDataloader):
        #try:
            loginpage = LoginPage(self.driver)
            loginpage.getLoginlink().click()
            loginpage.getLoginID().send_keys(LoginpageDataloader[0])
            loginpage.getPassword().send_keys(LoginpageDataloader[1])
            loginpage.getLoginButton().click()
            time.sleep(5)
            homepage = HomePage(self.driver)
            Imm_care_Title = homepage.ImmedieteCareHeaderHomePage().text
            #assert (Imm_care_Title == 'Immediate Care')
            if (Imm_care_Title == 'Immediate Care'):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
                assert False
            time.sleep(2)

    @pytest.fixture(
        params=[("prameela.b@lancesoft.com", "Password1234$")])
    def LoginpageDataloader(request):
        return request.param
















