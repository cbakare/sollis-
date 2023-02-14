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
class Test_HouseCall_CovidCare_VaccinationAppointments():
    @allure.title("Verify appointment creation for primary Member for Covid treatment From House call by selecting Primary address")
    def test_VerifyHouseCallAppointment_PrimaryMemberWithPrimaryAddress(self, setup,LoginpageDataloader):
        # try:
        base = BaseClass(self.driver)
        base.signin(setup)
        base.Login(LoginpageDataloader)
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
        for serv in Services:
            services1 = serv.text
            list_services_HouseCall.append(services1)
        print(list_services_HouseCall)
        common.selectCovidTreatementOptionRandomly().click()
        urgentcare = UrgentCare(self.driver)
        urgentcare.checkSubmitButtonisclickable().click()
        common.verifyPrimaryMemberName()
        common.VerifyRequestHouseCallHeader()
        common.houseCallPrimaryRequestaddress()
        common.houseCallSpecialInstruction()
        service = SelectServiceClinic(self.driver)
        service.getSubmitButtonAtSelectSelection().click()
        common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
        urgentcare.checkSubmitButtonisclickable().click()
        common.getAllUserdataintoListforHouseCall()
        # urgentcare.checkSubmitButtonisclickable().click()
        housecare.getSubmitRequestButton().click()
        time.sleep(2)

    @allure.title("Verify House call Treatment Appointment booking for primary member by selecting secondary address")
    def test_VerifyHouseCallTreatment_PrimaryMemberwithSecondaryAddress(self):
        # try:
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
        for serv in Services:
            services1 = serv.text
            list_services_HouseCall.append(services1)
        print(list_services_HouseCall)
        common.selectCovidTreatementOptionRandomly().click()
        urgentcare = UrgentCare(self.driver)
        urgentcare.checkSubmitButtonisclickable().click()
        common.verifyPrimaryMemberName()
        common.VerifyRequestHouseCallHeader()
        housecare.getOtherAlternetAddressForHouseCallRB().click()
        common.enterDetailForAlternetaddress()
        service = SelectServiceClinic(self.driver)
        service.getSubmitButtonAtSelectSelection().click()
        common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
        urgentcare.checkSubmitButtonisclickable().click()
        common.getAllUserdataintoListforHouseCall()
        # urgentcare.checkSubmitButtonisclickable().click()
        housecare.getSubmitRequestButton().click()
        time.sleep(2)

        # except Exception as e:
        allure.attach(self.driver.get_screenshot_as_png(), name="test_HouseCallAppointment",
                      attachment_type=AttachmentType.PNG)

    @allure.title(
        "Verify Appoint creation for dependant for Covid Treatment From House call by selecting Primary address")
    def test_VerifyHouseCallATreatment_DependantByselectingPrimaryAddress(self):
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
            common.selectCovidTreatementOptionRandomly().click()
            urgentcare = UrgentCare(self.driver)
            urgentcare.checkSubmitButtonisclickable().click()
            service = SelectServiceClinic(self.driver)
            service.getCrossMarkForSelectedMember().click()
            service.getDownArrowWhenNoMemberSelectedInMemberDropdown().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service.getSubmitButton().click()
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
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_HouseCallAppointment",
                          attachment_type=AttachmentType.PNG)

    @allure.title(
        "Verify Appoint creation for dependant for Covid Treatment From House call by selecting secondary address")
    def test_VerifyHouseCallTreatment_DependantByselectingSecAddress(self):
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
            for serv in Services:
                services1 = serv.text
                list_services_HouseCall.append(services1)
            print(list_services_HouseCall)
            common.selectCovidTreatementOptionRandomly().click()
            urgentcare = UrgentCare(self.driver)
            urgentcare.checkSubmitButtonisclickable().click()
            service = SelectServiceClinic(self.driver)
            service.getCrossMarkForSelectedMember().click()
            service.getDownArrowWhenNoMemberSelectedInMemberDropdown().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service.getSubmitButton().click()
            common.VerifyRequestHouseCallHeader()
            housecare.getOtherAlternetAddressForHouseCallRB().click()
            common.enterDetailForAlternetaddress()
            service.getSubmitButtonAtSelectSelection().click()
            common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
            urgentcare.checkSubmitButtonisclickable().click()
            common.getAllUserdataintoListforHouseCall()
            # urgentcare.checkSubmitButtonisclickable().click()
            housecare.getSubmitRequestButton().click()
            time.sleep(2)
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_HouseCallAppointment",
                          attachment_type=AttachmentType.PNG)