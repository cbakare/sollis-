from datetime import time
import time
from logging import Logger

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.BaseClass import BaseClass
from utility.Logger import logger

@pytest.mark.usefixtures("setup")
class Test_SpecialRefferance(logger):

    def test_verifyPrimeMemeberRefferalFlow(self,setup, LoginpageDataloader):
    #Verify Special refferal flow
        try:
            log=self.getLogger()
            base=BaseClass(self.driver)
            base.signin(setup)
            base.Login(LoginpageDataloader)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Specialist Referral']"))).click()
            Spc_Reff_header = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Specialist Referral']"))).text
            if (Spc_Reff_header == "Specialist Referral"):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
                assert False
            table_clm_header1 = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div/table/thead[1]/tr/th[1]/span"))).text
            if (table_clm_header1 == "SPECIALTY"):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
                assert False
            # table_clm_header2 = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div/table/thead[1]/tr/th[2]/span'))).text
            # if (table_clm_header2 == "STATUS"):
            #     assert True
            # else:
            #     allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
            #     assert False
            table_clm_header3 = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div/table/thead[1]/tr/th[2]/span'))).text
            if (table_clm_header3 == "REQUEST DATE"):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
                assert False
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="NEW REQUEST"]'))).click()
            NewReq_msg = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'referral request')]"))).text
            if ("Member needing a referral request" == NewReq_msg):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
                assert False
            # element=driver.find_element((By.XPATH,"//li[@class='nav-item']/a[1]"))
            # flag_22=(WebDriverWait(driver,5).until(EC.element_located_to_be_selected((By.XPATH,"//a[contains(@class,'nav-link') and text()='Prameela Himabindu']"))))
            a = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Prameela')]"))).is_displayed()
            print(a)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type a Specialist']"))).send_keys("car")
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type a Specialist']"))).send_keys(Keys.ARROW_DOWN)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type a Specialist']"))).send_keys(Keys.ENTER)
            time.sleep(2)
            Flag2 = self.driver.execute_script(f"return document.getElementById('Sollis').checked")
            print(Flag2)
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='mb-3']/textarea"))).send_keys("ADM test")
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='mb-3']/textarea"))).send_keys(Keys.DOWN)
            time.sleep(5)
            base=BaseClass(self.driver)
            base.ScrollDowntoPage()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Next']"))).click()
            time.sleep(10)

            # Message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h5[text()='Thank You!']"))).text
            # print(Message)
            #Message should be assert with DB
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1", attachment_type=AttachmentType.PNG)


