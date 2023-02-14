import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from PageObject.HouseCallCovidcare import HouseCallCovidCare
from PageObject.Multimember import Multimember
from PageObject.ScheduleAppClinic import ScheduleAppClinic
from PageObject.SelectServiceClinic import SelectServiceClinic
from PageObject.HouseCallImmedieteCare import UrgentCare_HouseCall
from PageObject.UrgentCareInClinic import UrgentCare
from utility.BaseClass import BaseClass
from utility.ScheduleCommonMethods import CommonMethod


@pytest.mark.usefixtures("setup")
class Test_HouseCall_ImmidieteCareVaccinationAppointments():
    @allure.title("House call - Verify new appointment creation for prime member from immediate care")
    def test_HouseCallImmidieteVerifyAppointmentCreation(self,setup,LoginpageDataloader):
        try:
            base = BaseClass(self.driver)
            base.signin(setup)
            base.Login(LoginpageDataloader)
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(2)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            common = CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            house_obj = UrgentCare_HouseCall(self.driver)
            house_obj.getHouseCallImmediateCarelink().click()
            common.getAppointmentConfirmPopup()
            Symptomlist = []
            Symptomlist = common.getListofPrimarySynptomps().copy()
            print(Symptomlist)
            urgentcare = UrgentCare(self.driver)
            urgentcare.getFirstSymptopns().click()
            time.sleep(5)
            urgentcare.checkSubmitButtonisclickable().click()
            member = Multimember(self.driver)
            member.getDropdownDownArow().click()
            time.sleep(2)
            Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
            member.selectCloseDDButton().click()
            service = SelectServiceClinic(self.driver)
            bydefault_member = house_obj.getPrimeMemberAtSelectMemberDropdownatHouseCall().text
            print(bydefault_member)
            assert (bydefault_member in Name_selectedMemeber)
            service.getSubmitButton().click()
            time.sleep(2)
            common.VerifyRequestHouseCallHeader()
            common.houseCallPrimaryRequestaddress()
            common.houseCallSpecialInstruction()
            service.getSubmitButtonAtSelectSelection().click()
            common.HouseCallrequestLoadingPhoneNumberAndPrefferedTiming()
            urgentcare.checkSubmitButtonisclickable().click()
            common.getAllUserdataintoListforHouseCall()
            # urgentcare.checkSubmitButtonisclickable().click()
            housecare = HouseCallCovidCare(self.driver)
            housecare.getSubmitRequestButton().click()
            time.sleep(2)
        except Exception as E:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)



    @allure.title("House call- Verify new appointment creation for prime member selecting secondary address")
    def test_HouseCallImmidieteVerifyAppointmentCreationwithsecAddress(self):
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
            common = CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            house_obj = UrgentCare_HouseCall(self.driver)
            house_obj.getHouseCallImmediateCarelink().click()
            common.getAppointmentConfirmPopup()
            Symptomlist = []
            Symptomlist = common.getListofPrimarySynptomps().copy()
            print(Symptomlist)
            urgentcare = UrgentCare(self.driver)
            urgentcare.getFirstSymptopns().click()
            time.sleep(5)
            urgentcare.checkSubmitButtonisclickable().click()
            member = Multimember(self.driver)
            member.getDropdownDownArow().click()
            time.sleep(2)
            Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
            member.selectCloseDDButton().click()
            service = SelectServiceClinic(self.driver)
            bydefault_member = house_obj.getPrimeMemberAtSelectMemberDropdownatHouseCall().text
            print(bydefault_member)
            assert (bydefault_member in Name_selectedMemeber)
            service.getSubmitButton().click()
            time.sleep(2)
            common.VerifyRequestHouseCallHeader()
            housecare = HouseCallCovidCare(self.driver)
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
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    @allure.title("House call - Verify new appointment creation for dependant from immediate care")
    def test_HouseCallImmidieteVerifyAppointmentCreationForDependant(self):
        try:
            home = HomePage(self.driver)
            time.sleep(2)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(2)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            common = CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            house_obj = UrgentCare_HouseCall(self.driver)
            house_obj.getHouseCallImmediateCarelink().click()
            common.getAppointmentConfirmPopup()
            Symptomlist = []
            Symptomlist = common.getListofPrimarySynptomps().copy()
            print(Symptomlist)
            urgentcare = UrgentCare(self.driver)
            urgentcare.getFirstSymptopns().click()
            time.sleep(5)
            urgentcare.checkSubmitButtonisclickable().click()
            service = SelectServiceClinic(self.driver)
            house_obj.getMemberDDDownArrowforHouseCallMemberDD().click()
            # service.getCrossMarkOfDDForSelf().click()
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
            housecare = HouseCallCovidCare(self.driver)
            housecare.getSubmitRequestButton().click()
            time.sleep(2)
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    @allure.title("House call- Verify new appointment creation for dependant from immediate care by selecting secondary address")
    def test_HouseCallImmidieteVerifyAppointmentCreationForDependantwithSecAddress(self):
        try:
            home = HomePage(self.driver)
            time.sleep(2)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(2)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            common = CommonMethod(self.driver)
            common.NavigatetoHousCallTab()
            house_obj = UrgentCare_HouseCall(self.driver)
            house_obj.getHouseCallImmediateCarelink().click()
            common.getAppointmentConfirmPopup()
            Symptomlist = []
            Symptomlist = common.getListofPrimarySynptomps().copy()
            print(Symptomlist)
            urgentcare = UrgentCare(self.driver)
            urgentcare.getFirstSymptopns().click()
            time.sleep(5)
            urgentcare.checkSubmitButtonisclickable().click()
            service = SelectServiceClinic(self.driver)
            house_obj.getMemberDDDownArrowforHouseCallMemberDD().click()
            # service.getCrossMarkOfDDForSelf().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service.getSubmitButton().click()
            common.VerifyRequestHouseCallHeader()
            housecare = HouseCallCovidCare(self.driver)
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
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)












