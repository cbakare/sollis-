import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from PageObject.HouseCallCovidcare import HouseCallCovidCare
from PageObject.ScheduleAppClinic import ScheduleAppClinic
from PageObject.SelectServiceClinic import SelectServiceClinic
from PageObject.UrgentCareInClinic import UrgentCare
from utility.BaseClass import BaseClass
from utility.ScheduleCommonMethods import CommonMethod

@pytest.mark.usefixtures("setup")
class Test_HouseCallCovidCare():
    @allure.title("House call-Verify Primary member is able to create a new appointment for covid Testing by selecting primary address")
    def test_HouseCall_VerifyPrimeMemberAppointmentCreation(self,setup,LoginpageDataloader):
        try:
            base = BaseClass(self.driver)
            base.signin(setup)
            base.Login(LoginpageDataloader)
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(2)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            header = scheduleApp.headerInClinic().text
            if header == "In-Clinic":
                assert  True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
                assert False
            common=CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            common.VerifyHouseCallHeader()
            common.NavigateToHouseCallCovidCare()
            common.getAppointmentConfirmPopup()
            time.sleep(10)
            housecare=HouseCallCovidCare(self.driver)
            Services=housecare.getAllOptionsAvailableUnderHouseCall()
            list_services_HouseCall=[]
            for service in Services:
                 services1=service.text
                 list_services_HouseCall.append(services1)
            print(list_services_HouseCall)
            common.verifySelectServiceclinicPageCovidTesting()
            urgentcare=UrgentCare(self.driver)
            urgentcare.checkSubmitButtonisclickable().click()
            common.verifyPrimaryMemberName()
    #        urgentcare.checkSubmitButtonisclickable().click()
            common.VerifyRequestHouseCallHeader()
            common.houseCallPrimaryRequestaddress()
            common.houseCallSpecialInstruction()
            service=SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
            urgentcare.checkSubmitButtonisclickable().click()
            common.getAllUserdataintoListforHouseCall()
            #urgentcare.checkSubmitButtonisclickable().click()
            housecare.getSubmitRequestButton().click()
            time.sleep(2)
           # housecare.getHouseCallViewAppointment().click()
        except Exception as E:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    @allure.title("House call-Verify new appointment creation for Primary member for covid Test by selecting secondary address")
    def test_HouseCall_VerifyPrimeMemberCovidTestAppointmentCreationbySelectingSecondaryAddress(self):
        try:
            home=HomePage(self.driver)
            time.sleep(2)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(2)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            header = scheduleApp.headerInClinic().text
            if (header == "In-Clinic"):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                                    attachment_type=AttachmentType.PNG)
                assert False
            common = CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            common.VerifyHouseCallHeader()
            common.NavigateToHouseCallCovidCare()
            common.getAppointmentConfirmPopup()
            housecare = HouseCallCovidCare(self.driver)
            Services = housecare.getAllOptionsAvailableUnderHouseCall()
            list_services_HouseCall = []
            for service in Services:
                services1 = service.text
                list_services_HouseCall.append(services1)
            print(list_services_HouseCall)
            common.verifySelectServiceclinicPageCovidTesting()
            urgentcare = UrgentCare(self.driver)
            urgentcare.checkSubmitButtonisclickable().click()
            common.verifyPrimaryMemberName()
            #urgentcare.checkSubmitButtonisclickable().click()
            common.VerifyRequestHouseCallHeader()
            housecare.getOtherAlternetAddressForHouseCallRB().click()
            common.enterDetailForAlternetaddress()
            service1=SelectServiceClinic(self.driver)
            service1.getSubmitButtonAtSelectSelection().click()
            common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
            urgentcare.checkSubmitButtonisclickable().click()
            common.getAllUserdataintoListforHouseCall()
            # urgentcare.checkSubmitButtonisclickable().click()
            housecare.getSubmitRequestButton().click()
            time.sleep(2)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_HouseCallAppointment",
                          attachment_type=AttachmentType.PNG)

    @allure.title(
        "House call-Verify new appointment creation for dependant member for covid Test by selecting primary address")
    def test_HouseCall_VerifyDependantAppointmentCreation(self):
        try:
            home = HomePage(self.driver)
            time.sleep(2)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(2)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            header = scheduleApp.headerInClinic().text
            if header == "In-Clinic":
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            common = CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            common.VerifyHouseCallHeader()
            common.NavigateToHouseCallCovidCare()
            common.getAppointmentConfirmPopup()
            time.sleep(10)
            housecare = HouseCallCovidCare(self.driver)
            Services = housecare.getAllOptionsAvailableUnderHouseCall()
            list_services_HouseCall = []
            for service in Services:
                services1 = service.text
                list_services_HouseCall.append(services1)
            print(list_services_HouseCall)
            common.verifySelectServiceclinicPageCovidTesting()
            urgentcare = UrgentCare(self.driver)
            urgentcare.checkSubmitButtonisclickable().click()
            service = SelectServiceClinic(self.driver)
            service.getMemberDDDownArrow().click()
            # service.getCrossMarkOfDDForSelf().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service.getSubmitButton().click()
            #urgentcare.checkSubmitButtonisclickable().click()
            common.VerifyRequestHouseCallHeader()
            common.houseCallPrimaryRequestaddress()
            common.houseCallSpecialInstruction()
            service.getSubmitButtonAtSelectSelection().click()
            common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
            urgentcare.checkSubmitButtonisclickable().click()
            common.getAllUserdataintoListforHouseCall()
            # urgentcare.checkSubmitButtonisclickable().click()
            housecare.getSubmitRequestButton().click()
            time.sleep(2)
        # housecare.getHouseCallViewAppointment().click()
            housecare.getSubmitRequestButton().click()
        except Exception as E:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    @allure.title("House call-Verify dependant application creation for Covid Test by updating the secondary Address")
    def test_HouseCall_VerifyDependantAppointmentCreationWithSecAddress(self):
        try:
            # base = BaseClass(self.driver)
            # base.signin(setup)
            # base.Login()
            home = HomePage(self.driver)
            time.sleep(2)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(2)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            header = scheduleApp.headerInClinic().text
            if (header == "In-Clinic"):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                                  attachment_type=AttachmentType.PNG)
                assert False
            common = CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            common.VerifyHouseCallHeader()
            common.NavigateToHouseCallCovidCare()
            common.getAppointmentConfirmPopup()
            housecare = HouseCallCovidCare(self.driver)
            Services = housecare.getAllOptionsAvailableUnderHouseCall()
            list_services_HouseCall = []
            for service in Services:
                services1 = service.text
                list_services_HouseCall.append(services1)
            print(list_services_HouseCall)
            common.verifySelectServiceclinicPageCovidTesting()
            urgentcare = UrgentCare(self.driver)
            urgentcare.checkSubmitButtonisclickable().click()
            service1 = SelectServiceClinic(self.driver)
            service1.getCrossMarkForSelectedMember().click()
                # service.getCrossMarkOfDDForSelf().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service1.getSubmitButton().click()
            # urgentcare.checkSubmitButtonisclickable().click()
            common.VerifyRequestHouseCallHeader()
            housecare.getOtherAlternetAddressForHouseCallRB().click()
            common.enterDetailForAlternetaddress()
            service1 = SelectServiceClinic(self.driver)
            service1.getSubmitButtonAtSelectSelection().click()
            common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
            urgentcare.checkSubmitButtonisclickable().click()
            common.getAllUserdataintoListforHouseCall()
            # urgentcare.checkSubmitButtonisclickable().click()
            housecare.getSubmitRequestButton().click()
            time.sleep(2)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_HouseCallAppointment",
                              attachment_type=AttachmentType.PNG)











