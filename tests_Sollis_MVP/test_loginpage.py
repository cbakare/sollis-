import time
# from datetime import timedelta,date

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

# from PageObject.AppointmentConfDetails import AppointmentDetails
from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
# from PageObject.Multimember import Multimember
# from PageObject.ScheduleAppClinic import ScheduleAppClinic
# from PageObject.SelectServiceClinic import SelectServiceClinic
# from utility.BaseClass import BaseClass



#@pytest.mark.usefixtures("setup")
#@pytest.mark.usefixtures("LoginpageDataloader")
from utility.Logger import logger

@pytest.mark.usefixtures("setup")
class Test_one(logger):
    @allure.title("Verify Login with proper credential")
    def test_VerifyLoginpage(self,setup, LoginpageDataloader):
        try:
            log=self.getLogger()
            log.info("Launching the url")
            WebDriverWait(self.driver, 10).until(EC.title_contains("Member Portal"))
            time.sleep(2)
            # self.driver.refresh()
            # time.sleep(2)
            log.info("getting the login page" )
            loginpage=LoginPage(self.driver)
            log.info("clicking on the Login link")
            loginpage.getLoginlink().click()
            #self.driver.refresh()
            time.sleep(2)
            loginpage.getLoginID().send_keys(LoginpageDataloader[0])
            loginpage.getPassword().send_keys(LoginpageDataloader[1])
            time.sleep(2)
            log.info("clicking the login button after entering cred")
            loginpage.getLoginButton().click()
            time.sleep(2)
            log.info("get homePage details")
            homepage=HomePage(self.driver)
            Imm_care_Title= homepage.ImmedieteCareHeaderHomePage().text
            assert (Imm_care_Title == 'Immediate Care')
            # Alert(self.driver).dismiss()
            time.sleep(2)
        except TimeoutException:
                self.driver.refresh()
                time.sleep(5)


           # Alert.dismiss()
        # except Exception as E:
        #     allure.attach(self.driver.get_screenshot_as_png(), name="LoginError",attachment_type=AttachmentType.PNG)
        #     assert False


























































