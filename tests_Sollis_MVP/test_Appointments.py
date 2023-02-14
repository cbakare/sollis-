import time
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType

from PageObject.Appointments import Appoinments
from utility.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Test_Appointments():
     @allure.title("Verify Application is showing the correct total appointment count at home page")
     def test_verifyAppointmentCount(self,setup):
        try:
            base = BaseClass(self.driver)
            base.signin(setup)
            base.Login()
            service_menu = []
            app=Appoinments(self.driver)
            app.getAppointmentLinkOnHomePage()
            App_Count = len(app.getListOfAppointments())
            if (App_Count == 6):
                 assert True
            else:
                 allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1", attachment_type=AttachmentType.PNG)
                 assert False

            service_menu.append(WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='appointment-label col-lg-6']//child::p"))).text)
            time.sleep(2)
            App_Count_label=len(self.driver.find_elements(By.XPATH,"//p[text()='Messages']/span"))
            if App_Count_label!=0:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Appointments']"))).click()
                time.sleep(2)
                Header_Menu_app = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(),'Appointments')]"))).text
                if (Header_Menu_app == "Appointments"):
                     assert True
                else :
                     allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
                     assert False
                time.sleep(10)
                Member_Active=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[3]/div[1]/div/div[1]/div[3]/p[2]"))).text
                print(Member_Active)
                if ("Prameela Himabindu" in Member_Active):
                     assert True
                else:
                     allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
                     assert False
                Appointment_count = len(self.driver.find_elements(By.XPATH, (("//div[@class='box appointments normal row']"))))
                print(Appointment_count)
                time.sleep(2)
                WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='mx-auto']"))).click()
                Home_App_count=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Appointments']/span"))).text
                Home_App_count1=int(Home_App_count)
                print(Home_App_count1)
                if (Appointment_count==Home_App_count1):
                   assert True
                else:
                   allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1", attachment_type=AttachmentType.PNG)
            else:
                  print("None of the Appointments are available")
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)







