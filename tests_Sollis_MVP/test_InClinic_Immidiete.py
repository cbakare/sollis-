import random
import time
import allure

import pytest
from _socket import timeout
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from PageObject.AppointmentConfDetails import AppointmentDetails
from PageObject.HomePage import HomePage
from PageObject.ScheduleAppClinic import ScheduleAppClinic
from PageObject.SelectServiceClinic import SelectServiceClinic
from PageObject.UrgentCareInClinic import UrgentCare
from utility.BaseClass import BaseClass
from utility.ScheduleCommonMethods import CommonMethod


@pytest.mark.usefixtures("setup")
class Test_UrgentCare():
    def test_verifyUrgentCareScheduleAppointment(self, setup, LoginpageDataloader):
        try:
            base = BaseClass(self.driver)
            base.signin(setup)
            base.Login(LoginpageDataloader)
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            schedule = ScheduleAppClinic(self.driver)
            # schedule.NavigateToScheduleAppoPage().click()
            time.sleep(5)
            schedule.getImmidieteCarelink().click()
            common.getAppointmentConfirmPopup()
            Symptomlist = []
            Symptomlist = common.getListofPrimarySynptomps().copy()
            print(Symptomlist)
            urgentcare = UrgentCare(self.driver)
            urgentcare.getFirstSymptopns().click()
            time.sleep(5)
            urgentcare.checkSubmitButtonisclickable().click()
            common.verifyPrimaryMemberName()
            common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            time.sleep(5)
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            time.sleep(2)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    def test_AppointmentPopUpCovidSelectingNo(self, setup, LoginpageDataloader):
            base=BaseClass(self.driver)
            base.signin(setup)
            base.Login(LoginpageDataloader)
        # try:
            time.sleep(5)
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            time.sleep(5)
            common = CommonMethod(self.driver)
            schedule = ScheduleAppClinic(self.driver)
            common.navigateToScheduleAppointment()
            time.sleep(5)
            schedule.getImmidieteCarelink().click()
            common.appointmentConfirmPopupWithNoOption()
            Symptomlist = []
            Symptomlist = common.getListofPrimarySynptomps().copy()
            print(Symptomlist)
            urgentcare = UrgentCare(self.driver)
            urgentcare.getFirstSymptopns().click()
            time.sleep(5)
            urgentcare.checkSubmitButtonisclickable().click()
            common.verifyPrimaryMemberNameForSingleSelect()
            common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            time.sleep(2)
        # except TimeoutException:
        #     allure.attach(self.driver.get_screenshot_as_png(), name="Immediate1",
        #                   attachment_type=AttachmentType.PNG)

    def test_InClinic_VerifyImmediateCareCovidTestAppointmentForDependant(self):
        try:
            home=HomePage(self.driver)
            home.getHomePageLogo().click()
            time.sleep(2)
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            schedule = ScheduleAppClinic(self.driver)
            # schedule.NavigateToScheduleAppoPage().click()
            time.sleep(5)
            schedule.getImmidieteCarelink().click()
            common.getAppointmentConfirmPopup()
            Symptomlist = []
            Symptomlist = common.getListofPrimarySynptomps().copy()
            print(Symptomlist)
            urgentcare = UrgentCare(self.driver)
            urgentcare.getFirstSymptopns().click()
            time.sleep(5)
            urgentcare.checkSubmitButtonisclickable().click()
            service=SelectServiceClinic(self.driver)
            service.getMemberDDDownArrow().click()
           # service.getCrossMarkOfDDForSelf().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service.getSubmitButton().click()
            common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            time.sleep(2)
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    def test_inClinicImmediate_VerifyNewAppointmentBookingByDefaultLocationAndChangingClinic(self):
        try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            schedule = ScheduleAppClinic(self.driver)
            time.sleep(2)
            schedule.getImmidieteCarelink().click()
            common.getAppointmentConfirmPopup()
            urgentcare = UrgentCare(self.driver)
            time.sleep(2)
            urgentcare.getFirstSymptopns().click()
            time.sleep(2)
            urgentcare.checkSubmitButtonisclickable().click()
            service = SelectServiceClinic(self.driver)
            service.getMemberDropdownArrowfromSelectAppointmentPage().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service.getSubmitButton().click()
            self.driver.refresh()
            time.sleep(10)
            service = SelectServiceClinic(self.driver)
            text_selected = service.getBydefaultSelectedValueInDD().text
            print(text_selected)
            assert (text_selected == "NY")
            basepage = BaseClass(self.driver)
            basepage.ScrollDowntoPage()
            defaultClinic = service.getNY_BydefaultselectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
            common.GetAllVailableDatesSlots()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            time.sleep(2)
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    def test_inClinicImmediate_VerifyNewAppointmentByChangingLocationAndClinic(self):
        try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            time.sleep(2)
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            schedule = ScheduleAppClinic(self.driver)
            time.sleep(2)
            schedule.getImmidieteCarelink().click()
            common.getAppointmentConfirmPopup()
            urgentcare = UrgentCare(self.driver)
            time.sleep(2)
            urgentcare.getFirstSymptopns().click()
            time.sleep(2)
            urgentcare.checkSubmitButtonisclickable().click()
            service = SelectServiceClinic(self.driver)
            service.getMemberDropdownArrowfromSelectAppointmentPage().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[3]").click()
            service.getSubmitButton().click()
            time.sleep(2)
            service = SelectServiceClinic(self.driver)
            service.getBydefaultSelectedValueInDD().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'-option-0')]").click()
            service.getOther_BydefaultSelectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
            common.GetAllVailableDatesSlots()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
        except Exception as E:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)




















