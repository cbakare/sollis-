import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from PageObject.AppointmentConfDetails import AppointmentDetails
from PageObject.HomePage import HomePage
from PageObject.HouseCallCovidcare import HouseCallCovidCare
from PageObject.HouseCallImmedieteCare import UrgentCare_HouseCall
from PageObject.Multimember import Multimember
from PageObject.ScheduleAppClinic import ScheduleAppClinic
from PageObject.UrgentCareInClinic import UrgentCare
from PageObject.VaccinationClinic import InClinic_Vaccination
from PageObject.SelectServiceClinic import SelectServiceClinic
from utility.BaseClass import BaseClass
from utility.ScheduleCommonMethods import CommonMethod


@pytest.mark.usefixtures("setup")
class Test_HouseCall_VaccinationCare():
    @allure.title("House call Vaccination Care -Verify Member is able to book an appointment by selecting primary address")
    def test_HouseCall_VaccinationCare_VerifyNewRequestSubmissionForMember(self,setup,LoginpageDataloader):
        # try:
        base = BaseClass(self.driver)
        base.signin(setup)
        base.Login(LoginpageDataloader)
        scheduleApp = ScheduleAppClinic(self.driver)
        time.sleep(2)
        scheduleApp.NavigateToScheduleAppointmentPage().click()
        common = CommonMethod(self.driver)
        common.NavigatetoHousCallTab()
        vaccination = InClinic_Vaccination(self.driver)
        vaccination.getInClinicVaccinationLink().click()
        common.getAppointmentConfirmPopup()
        common.getVaccinationListUnderVaccinationModule().click()
        urgentcare = UrgentCare(self.driver)
        urgentcare.checkSubmitButtonisclickable().click()
        member = Multimember(self.driver)
        member.getDropdownDownArow().click()
        time.sleep(2)
        Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
        member.selectCloseDDButton().click()
        service = SelectServiceClinic(self.driver)
        house_obj=UrgentCare_HouseCall(self.driver)
        bydefault_member = house_obj.getPrimeMemberAtSelectMemberDropdownatHouseCall().text
        print(bydefault_member)
        assert (bydefault_member in Name_selectedMemeber)
        service.getSubmitButtonAtSelectSelection().click()
        time.sleep(2)
        common.VerifyRequestHouseCallHeader()
        common.houseCallPrimaryRequestaddress()
        common.houseCallSpecialInstruction()
        service.getSubmitButtonAtSelectSelection().click()
        common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
        service.getSubmitButtonAtSelectSelection().click()
        common.getAllUserdataintoListforHouseCall()
        # urgentcare.checkSubmitButtonisclickable().click()
        housecare = HouseCallCovidCare(self.driver)
        housecare.getSubmitRequestButton().click()
        time.sleep(5)
        Flag=housecare.getHouseCallSubmitRequestConfirmationHeader().is_displayed()
        if Flag==True :
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                        attachment_type=AttachmentType.PNG)

    @allure.title("House call- Vaccination care- Verify new appointment creation for prime member by selecting secondary address")
    def test_HouseCallVaccinationCare_AppointmentCreationwithsecAddress(self):
            # base = BaseClass(self.driver)
            # base.signin(setup)
            # base.Login()
            home = HomePage(self.driver)
            time.sleep(2)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(2)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            common = CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            vaccination = InClinic_Vaccination(self.driver)
            vaccination.getInClinicVaccinationLink().click()
            common.getAppointmentConfirmPopup()
            common.getVaccinationListUnderVaccinationModule().click()
            service1 = SelectServiceClinic(self.driver)
            urgentcare = UrgentCare(self.driver)
            urgentcare.checkSubmitButtonisclickable().click()
            member = Multimember(self.driver)
            member.getDropdownDownArow().click()
            time.sleep(2)
            Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
            member.selectCloseDDButton().click()
            service = SelectServiceClinic(self.driver)
            house_obj = UrgentCare_HouseCall(self.driver)
            bydefault_member = house_obj.getPrimeMemberAtSelectMemberDropdownatHouseCall().text
            print(bydefault_member)
            assert (bydefault_member in Name_selectedMemeber)
            service1.getSubmitButtonAtSelectSelection().click()
            time.sleep(2)
            common.VerifyRequestHouseCallHeader()
            housecare = HouseCallCovidCare(self.driver)
            housecare.getOtherAlternetAddressForHouseCallRB().click()
            common.enterDetailForAlternetaddress()
            service1.getSubmitButtonAtSelectSelection().click()
            common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
            service1.getSubmitButtonAtSelectSelection().click()
            common.getAllUserdataintoListforHouseCall()
            # urgentcare.checkSubmitButtonisclickable().click()
            housecare.getSubmitRequestButton().click()
            time.sleep(5)
            Flag = housecare.getHouseCallSubmitRequestConfirmationHeader().is_displayed()
            if Flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    @allure.title("House call - Vaccination care - Verify new appointment creation for dependant")
    def test_HouseCallVaccinationCare_AppointmentCreationForDependant(self):
            home = HomePage(self.driver)
            time.sleep(2)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(2)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            common = CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            vaccination = InClinic_Vaccination(self.driver)
            vaccination.getInClinicVaccinationLink().click()
            common.getAppointmentConfirmPopup()
            common.getVaccinationListUnderVaccinationModule().click()
            service = SelectServiceClinic(self.driver)
            urgentcare = UrgentCare(self.driver)
            urgentcare.checkSubmitButtonisclickable().click()
            house_obj = UrgentCare_HouseCall(self.driver)
            house_obj.getMemberDDDownArrowforHouseCallMemberDD().click()
            # service.getCrossMarkOfDDForSelf().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service.getSubmitButtonAtSelectSelection().click()
            common.VerifyRequestHouseCallHeader()
            common.houseCallPrimaryRequestaddress()
            common.houseCallSpecialInstruction()
            service.getSubmitButtonAtSelectSelection().click()
            common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
            service.getSubmitButtonAtSelectSelection().click()
            common.getAllUserdataintoListforHouseCall()
            # urgentcare.checkSubmitButtonisclickable().click()
            housecare = HouseCallCovidCare(self.driver)
            housecare.getSubmitRequestButton().click()
            time.sleep(5)
            Flag = housecare.getHouseCallSubmitRequestConfirmationHeader().is_displayed()
            if Flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)

            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    @allure.title(
        "House call Vaccination Care- Verify new appointment creation for dependant by selecting secondary address")
    def test_HouseCallVaccinationCare_AppointmentCreationForDependantwithSecAddress(self):
            home = HomePage(self.driver)
            time.sleep(2)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(2)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            common = CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            vaccination = InClinic_Vaccination(self.driver)
            vaccination.getInClinicVaccinationLink().click()
            common.getAppointmentConfirmPopup()
            common.getVaccinationListUnderVaccinationModule().click()
            service1 = SelectServiceClinic(self.driver)
            urgentcare = UrgentCare(self.driver)
            urgentcare.checkSubmitButtonisclickable().click()
            house_obj = UrgentCare_HouseCall(self.driver)
            house_obj.getMemberDDDownArrowforHouseCallMemberDD().click()
            # service.getCrossMarkOfDDForSelf().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service1.getSubmitButtonAtSelectSelection().click()
            common.VerifyRequestHouseCallHeader()
            housecare = HouseCallCovidCare(self.driver)
            housecare.getOtherAlternetAddressForHouseCallRB().click()
            common.enterDetailForAlternetaddress()
            service1.getSubmitButtonAtSelectSelection().click()
            common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
            service1.getSubmitButtonAtSelectSelection().click()
            common.getAllUserdataintoListforHouseCall()
            housecare.getSubmitRequestButton().click()
            time.sleep(5)
            Flag = housecare.getHouseCallSubmitRequestConfirmationHeader().is_displayed()
            if Flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)








