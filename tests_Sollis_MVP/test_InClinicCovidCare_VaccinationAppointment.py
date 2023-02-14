import time
from datetime import date
import pytest
from allure_commons.types import AttachmentType
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from PageObject.AppointmentConfDetails import AppointmentDetails
from PageObject.HomePage import HomePage
from PageObject.Multimember import Multimember
from PageObject.ScheduleAppClinic import ScheduleAppClinic
from PageObject.SelectServiceClinic import SelectServiceClinic
from utility.BaseClass import BaseClass
from utility.Logger import logger
from utility.ScheduleCommonMethods import CommonMethod
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.mark.usefixtures("setup")
class Test_ClinicApp():
    @allure.title("In Clinic- Verify Primary prime Member appointment creation for Covid Vaccination")
    def test_InClinicCovidCare_PrimeMemberNewAppointmentCreationForCovidVaccination(self, setup, LoginpageDataloader):
        #try:
            base=BaseClass(self.driver)
            #log= self.logger()
            #log.info("logging in")
            base.signin(setup)
            #log.info("login")
            base.Login(LoginpageDataloader)
            #log.info("navigation")
            common=CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            time.sleep(5)
            #log.info("scheduleApp")
            scheduleApp = ScheduleAppClinic(self.driver)
            scheduleApp.getCovidCarelinkclinic().click()
            common.getAppointmentConfirmPopup()
            time.sleep(2)
            common.getAllVaccinationList()
            Selected_Vaccination=common.selectvaccinationRandomly()
            Selected_Vaccination.click()
            selected_dose=common.getAlldosesforSelectedVaccine()
            selected_dose.click()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            #common.getallVacinationlist()
            # common.VaccineSelected()
            # time.sleep(2)
            #common.verifyallVaccinationOptions()
            common.verifyPrimaryMemberName()
            common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            time.sleep(5)
            flag = detailConf.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="ClinicAppointment",
                              attachment_type=AttachmentType.PNG)


    @allure.title("In Clinic- Verify dependant Member appointment creation for Covid Vaccination")
    def test_InClinicCovidCare_VerifyNewAppointmentCreationForCovidVaccinationForDependant(self):
            home=HomePage(self.driver)
            home.getHomePageLogo().click()
            #log.info("navigation")
            common=CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            time.sleep(5)
            #log.info("scheduleApp")
            scheduleApp = ScheduleAppClinic(self.driver)
            scheduleApp.getCovidCarelinkclinic().click()
            common.getAppointmentConfirmPopup()
            time.sleep(2)
            common.getAllVaccinationList()
            Selected_Vaccination=common.selectvaccinationRandomly()
            Selected_Vaccination.click()
            selected_dose=common.getAlldosesforSelectedVaccine()
            selected_dose.click()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            service.getCrossMarkForSelectedMember().click()
            service. getDownArrowWhenNoMemberSelectedInMemberDropdown().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[3]").click()
            service.getSubmitButtonAtSelectSelection().click()
            common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            #service.getSubmitButtonatSelectSelection().click()
            time.sleep(5)
            flag = detailConf.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)

    @allure.title("In Clinic- Verify Primary and dependant Member appointment creation together for Covid Vaccination")
    def test_InClinicCovidCare_NewAppointmentCreationForCovidVaccinationForPrimeMemberAndDependant(self):
        try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            # log.info("navigation")
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            time.sleep(5)
            # log.info("scheduleApp")
            scheduleApp = ScheduleAppClinic(self.driver)
            scheduleApp.getCovidCarelinkclinic().click()
            common.getAppointmentConfirmPopup()
            time.sleep(2)
            common.getAllVaccinationList()
            Selected_Vaccination = common.selectvaccinationRandomly()
            Selected_Vaccination.click()
            selected_dose = common.getAlldosesforSelectedVaccine()
            selected_dose.click()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            service.ClickOnTheDropdownForMember().click()
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service.getSubmitButtonAtSelectSelection().click()
            common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            # service.getSubmitButtonatSelectSelection().click()
            time.sleep(5)
            flag = detailConf.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
        except Exception as E:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    @allure.title("In Clinic- Verify Primary Member appointment creation for Covid Vaccination by changing clinic")
    def test_InClinicCovidCare_NewAppointmentCreationForPrimaryMemberWithDefaultLocationAndChangingClinic(self):
        try:
            home=HomePage(self.driver)
            home.getHomePageLogo().click()
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            time.sleep(5)
            # log.info("scheduleApp")
            scheduleApp = ScheduleAppClinic(self.driver)
            scheduleApp.getCovidCarelinkclinic().click()
            common.getAppointmentConfirmPopup()
            time.sleep(2)
            common.getAllVaccinationList()
            Selected_Vaccination = common.selectvaccinationRandomly()
            Selected_Vaccination.click()
            selected_dose = common.getAlldosesforSelectedVaccine()
            selected_dose.click()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            common.verifyPrimaryMemberName()
            text_selected = service.getBydefaultSelectedValueInDD().text
            print(text_selected)
            basepage = BaseClass(self.driver)
            basepage.ScrollDowntoPage()
            defaultClinic = service.getNY_BydefaultselectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            # service.getSubmitButtonatSelectSelection().click()
            time.sleep(2)
        except Exception as E:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    @allure.title("In Clinic- Verify dependant appointment creation for Covid Vaccination by changing clinic")
    def test_InClinicCovidCare_NewAppointmentCreationForVaccinationForDependantByChangingClinic(self):
        try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            time.sleep(2)
            # log.info("navigation")
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            time.sleep(5)
            # log.info("scheduleApp")
            scheduleApp = ScheduleAppClinic(self.driver)
            scheduleApp.getCovidCarelinkclinic().click()
            common.getAppointmentConfirmPopup()
            time.sleep(2)
            common.getAllVaccinationList()
            Selected_Vaccination = common.selectvaccinationRandomly()
            Selected_Vaccination.click()
            selected_dose = common.getAlldosesforSelectedVaccine()
            selected_dose.click()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            service.getCrossMarkForSelectedMember().click()
            service.getDownArrowWhenNoMemberSelectedInMemberDropdown().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[3]").click()
            service.getSubmitButtonAtSelectSelection()
            text_selected = service.getBydefaultSelectedValueInDD().text
            print(text_selected)
            basepage = BaseClass(self.driver)
            basepage.ScrollDowntoPage()
            defaultClinic = service.getNY_BydefaultselectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
           # common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            # service.getSubmitButtonatSelectSelection().click()
            time.sleep(2)
        except Exception as E:
             allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                           attachment_type=AttachmentType.PNG)

    @allure.title("In Clinic- Verify Primary and dependant Member appointment creation together for Covid Vaccination by changing clinic")
    def test_InClinicCovidCare_NewAppointmentCreationForCovidVaccinationForPrimeMemberAndDependantByChangingClinic(self):
        try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            # log.info("navigation")
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            time.sleep(5)
            # log.info("scheduleApp")
            scheduleApp = ScheduleAppClinic(self.driver)
            scheduleApp.getCovidCarelinkclinic().click()
            common.getAppointmentConfirmPopup()
            time.sleep(2)
            common.getAllVaccinationList()
            Selected_Vaccination = common.selectvaccinationRandomly()
            Selected_Vaccination.click()
            selected_dose = common.getAlldosesforSelectedVaccine()
            selected_dose.click()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            service.ClickOnTheDropdownForMember().click()
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service.getSubmitButtonAtSelectSelection().click()
            text_selected = service.getBydefaultSelectedValueInDD().text
            print(text_selected)
            basepage = BaseClass(self.driver)
            basepage.ScrollDowntoPage()
            defaultClinic = service.getNY_BydefaultselectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
            # common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            time.sleep(5)
            flag = detailConf.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)

        except Exception as E:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                  attachment_type=AttachmentType.PNG)

    @allure.title("In Clinic- Verify Primary prime Member appointment creation for Covid Vaccination by Changing State abd Clinic")
    def test_InClinicCovidCare_PrimeMemberNewAppointmentCreationForCovidVaccinationByChangingStateAndClinic(self, setup):
        try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            time.sleep(5)
            # log.info("scheduleApp")
            scheduleApp = ScheduleAppClinic(self.driver)
            scheduleApp.getCovidCarelinkclinic().click()
            common.getAppointmentConfirmPopup()
            time.sleep(2)
            common.getAllVaccinationList()
            Selected_Vaccination = common.selectvaccinationRandomly()
            Selected_Vaccination.click()
            selected_dose = common.getAlldosesforSelectedVaccine()
            selected_dose.click()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            # common.getallVacinationlist()
            # common.VaccineSelected()
            # time.sleep(2)
            #common.verifyallVaccinationOptions()
            common.verifyPrimaryMemberName()
            service = SelectServiceClinic(self.driver)
            service.getBydefaultSelectedValueInDD().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'-option-0')]").click()
            service.getOther_BydefaultSelectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
            schedule = ScheduleAppClinic(self.driver)
            flag = schedule.getFirstRadioButtonUnderAvailableSlot().is_selected
            print(flag)
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            time.sleep(5)
            flag = detailConf.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)

        except Exception as E:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                      attachment_type=AttachmentType.PNG)

    @allure.title("In Clinic- Verify dependant Member appointment creation for Covid Vaccination by changing state and clinic")
    def test_InClinicCovidCare_VerifyNewAppointmentCreationForCovidVaccinationForDependantByChangingStateAndClinic (self):
        try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            # log.info("navigation")
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            time.sleep(5)
            # log.info("scheduleApp")
            scheduleApp = ScheduleAppClinic(self.driver)
            scheduleApp.getCovidCarelinkclinic().click()
            common.getAppointmentConfirmPopup()
            time.sleep(2)
            common.getAllVaccinationList()
            Selected_Vaccination = common.selectvaccinationRandomly()
            Selected_Vaccination.click()
            selected_dose = common.getAlldosesforSelectedVaccine()
            selected_dose.click()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            service.getCrossMarkForSelectedMember().click()
            service.getDownArrowWhenNoMemberSelectedInMemberDropdown().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[3]").click()
            service.getSubmitButtonAtSelectSelection().click()
            service = SelectServiceClinic(self.driver)
            service.getBydefaultSelectedValueInDD().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'-option-0')]").click()
            service.getOther_BydefaultSelectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
            schedule = ScheduleAppClinic(self.driver)
            flag = schedule.getFirstRadioButtonUnderAvailableSlot().is_selected
            print(flag)
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            time.sleep(5)
            flag = detailConf.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)

        except Exception as E:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                      attachment_type=AttachmentType.PNG)


















