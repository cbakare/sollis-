import time

import allure
import pytest
from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from PageObject.Multimember import Multimember
from PageObject.VaccinationClinic import InClinic_Vaccination
from PageObject.ScheduleAppClinic import ScheduleAppClinic
from PageObject.SelectServiceClinic import SelectServiceClinic
from utility.BaseClass import BaseClass
from utility.ScheduleCommonMethods import CommonMethod

@pytest.mark.usefixtures("setup")
class  Test_HouseCall_preventiveCare():
    def test_InClinic_PreventativeCare_VerifyNewRequestSubmissionForMember(self,setup):
        base = BaseClass(self.driver)
        base.signin(setup)
        base.Login()
        preventive = InClinic_Vaccination(self.driver)
        common =CommonMethod(self.driver)
        common.navigateToScheduleAppointment()
        common.NavigatetoHousCallTab()
        time.sleep(2)
        preventive.getInClinicVaccinationLink().click()
        common.getAppointmentConfirmPopup()
        member =ember = Multimember(self.driver)
        member.getDropdownDownArow().click()
        time.sleep(2)
        Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
        print(Name_selectedMemeber)
        member.selectCloseDDButton().click()
        service = SelectServiceClinic(self.driver)
        bydefault_member = service.primarySelectMemberForTreatmentDD().text
        print(bydefault_member)
        assert (bydefault_member in Name_selectedMemeber)
        preventive.getInClinicVaccinationDescribeYourSymptomsTextbox().send_keys("Offshore Automation Testing")
        preventive.getInClinicPreventiveSubmitRequestButton().click()
        Header_text =preventive.getInClinicPreventiveHeaderTextForSchedulingText().text
        assert(Header_text =="Scheduling Confirmation")
        Confirmation_Message =preventive.getInClinicPreventiveSchedulingConfirmationMessage().text
        print(Confirmation_Message)

    def test_InClinic_PreventativeCare_VerifyNewRequestSubmissionForDependantandMember(self ,setup):
        home =HomePage(self.driver)
        home.getHomePageLogo().click()
        common = CommonMethod(self.driver)
        common.navigateToScheduleAppointment()
        common.NavigatetoHousCallTab()
        time.sleep(2)
        preventive = InClinic_Vaccination(self.driver)
        preventive.getInClinicVaccinationLink().click()
        common.getAppointmentConfirmPopup()
        service = SelectServiceClinic(self.driver)
        service.ClickOntheDropdownForMember().click()
        self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[3]").click()
        preventive.getInClinicVaccinationDescribeYourSymptomsTextbox().send_keys("Offshore Automation Testing for dependant")
        preventive.getInClinicPreventiveSubmitRequestButton().click()
        Header_text = preventive.getInClinicPreventiveHeaderTextForSchedulingText().text
        assert (Header_text == "Scheduling Confirmation")
        Confirmation_Message = preventive.getInClinicPreventiveSchedulingConfirmationMessage().text
        print(Confirmation_Message)

    def test_InClinic_PreventativeCare_VerifyNewRequestSubmissionForDependantant(self ,setup):
        home = HomePage(self.driver)
        home.getHomePageLogo().click()
        preventive = InClinic_Vaccination(self.driver)
        common = CommonMethod(self.driver)
        common.navigateToScheduleAppointment()
        common.NavigatetoHousCallTab()
        time.sleep(2)
        preventive.getInClinicVaccinationLink().click()
        common.getAppointmentConfirmPopup()
        self.driver.find_element(By.XPATH ,"//div[@class='css-xb97g8']").click()
        self.driver.find_element(By.XPATH ,"//div[contains(@class,'-indicatorContainer')]").click()
        self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[3]").click()
        preventive.getInClinicVaccinationDescribeYourSymptomsTextbox().send_keys("Offshore Automation Testing for dependant")
        preventive.getInClinicPreventiveSubmitRequestButton().click()
        Header_text = preventive.getInClinicPreventiveHeaderTextForSchedulingText().text
        assert (Header_text == "Scheduling Confirmation")
        Confirmation_Message = preventive.getInClinicPreventiveSchedulingConfirmationMessage().text
        print(Confirmation_Message)
