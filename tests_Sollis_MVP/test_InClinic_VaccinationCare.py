import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from PageObject.AppointmentConfDetails import AppointmentDetails
from PageObject.HomePage import HomePage
from PageObject.Multimember import Multimember
from PageObject.ScheduleAppClinic import ScheduleAppClinic
from PageObject.UrgentCareInClinic import UrgentCare
from PageObject.VaccinationClinic import InClinic_Vaccination
from PageObject.SelectServiceClinic import SelectServiceClinic
from utility.BaseClass import BaseClass
from utility.ScheduleCommonMethods import CommonMethod


@pytest.mark.usefixtures("setup")
class Test_InClinic_VaccinationCare():
    @allure.title("Verify Member is able to book an appointment by selecting default clinic and State")
    def test_InClinic_VaccinationCare_VerifyNewRequestSubmissionForMember(self,setup,LoginpageDataloader):
            base = BaseClass(self.driver)
            base.signin(setup)
            base.Login(LoginpageDataloader)
            vaccination = InClinic_Vaccination(self.driver)
            common=CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            time.sleep(2)
            vaccination.getInClinicVaccinationLink().click()
            common.getAppointmentConfirmPopup()
            common.getVaccinationListUnderVaccinationModule().click()
            urgent=UrgentCare(self.driver)
            urgent.checkSubmitButtonisclickable().click()
            member = Multimember(self.driver)
            member.getDropdownDownArow().click()
            time.sleep(2)
            Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
            print(Name_selectedMemeber)
            member.selectCloseDDButton().click()
            service = SelectServiceClinic(self.driver)
            bydefault_member = service.primarySelectMemberForTreatmentDDforMultiselctValue().text
            print(bydefault_member)
            assert (bydefault_member in Name_selectedMemeber)
            time.sleep(5)
            service.getSubmitButtonAtSelectSelection().click()
            # vaccination.getInClinicVaccinationDescribeYourSymptomsTextbox().send_keys("Offshore Automation Testing")
            common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            Header_text=vaccination.getInClinicPreventiveHeaderTextForSchedulingText().text
            assert(Header_text=="Review Appointment Details")
            app=AppointmentDetails(self.driver)
            app.getConfirmationButton().click()
            time.sleep(2)
        # except Exception as e:
        #     print("exception found")
        #     allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
        #                   attachment_type=AttachmentType.PNG)

    @allure.title("In clinic Vaccination Care- Verify Member is able to book an appointment for dependant by selecting default clinic and State")
    def test_InClinic_Vaccination_VerifyNewRequestSubmissionForDependant(self):
        #try:
            home=HomePage(self.driver)
            home.getHomePageLogo().click()
            vaccination = InClinic_Vaccination(self.driver)
            common = CommonMethod(self.driver)
            time.sleep(5)
            common.navigateToScheduleAppointment()
            time.sleep(2)
            vaccination.getInClinicVaccinationLink().click()
            common.getAppointmentConfirmPopup()
            common.getVaccinationListUnderVaccinationModule().click()
            urgent = UrgentCare(self.driver)
            urgent.checkSubmitButtonisclickable().click()
            member = Multimember(self.driver)
            service = SelectServiceClinic(self.driver)
            service.getDownArrowWhenNoMemberSelectedInMemberDropdown().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[3]").click()
            service.getSubmitButtonAtSelectSelection().click()
            time.sleep(5)
            common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            Header_text=vaccination.getInClinicPreventiveHeaderTextForSchedulingText().text
            assert(Header_text=="Review Appointment Details")
            app = AppointmentDetails(self.driver)
            app.getConfirmationButton().click()
            time.sleep(2)

        # except Exception as e:
        #     allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
        #                   attachment_type=AttachmentType.PNG)

    @allure.title("In clinic Vaccination Care-Verify Member is able to book an appointment for self and dependant by selecting default clinic and State")
    def test_InClinic_Vaccination_NewRequestSubmissionForPrimeMemberandDependantTogether(self):
        try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            vaccination = InClinic_Vaccination(self.driver)
            common = CommonMethod(self.driver)
            time.sleep(5)
            common.navigateToScheduleAppointment()
            time.sleep(2)
            vaccination.getInClinicVaccinationLink().click()
            common.getAppointmentConfirmPopup()
            common.getVaccinationListUnderVaccinationModule().click()
            urgent = UrgentCare(self.driver)
            urgent.checkSubmitButtonisclickable().click()
            member = Multimember(self.driver)
            service = SelectServiceClinic(self.driver)
            service.getMemberDropdownArrowfromSelectAppointmentPage().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[3]").click()
            service.getSubmitButtonAtSelectSelection().click()
            #urgent.checkSubmitButtonisclickable().click()
            time.sleep(5)
            common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            Header_text = vaccination.getInClinicPreventiveHeaderTextForSchedulingText().text
            assert (Header_text == "Review Appointment Details")
            app = AppointmentDetails(self.driver)
            app.getConfirmationButton().click()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_VaccinationCare",
                      attachment_type=AttachmentType.PNG)

    @allure.title("In clinic Vaccination Care-Verify Member is able to book an appointment by changing Clinic")
    def test_InClinic_VaccinationCare_VerifyNewRequestSubmissionForSelfByChangingClinic(self,setup):
        # base = BaseClass(self.driver)
        # base.signin(setup)
        # base.Login()
        home = HomePage(self.driver)
        home.getHomePageLogo().click()
        vaccination = InClinic_Vaccination(self.driver)
        common = CommonMethod(self.driver)
        common.navigateToScheduleAppointment()
        time.sleep(2)
        vaccination.getInClinicVaccinationLink().click()
        common.getAppointmentConfirmPopup()
        common.getVaccinationListUnderVaccinationModule().click()
        urgent = UrgentCare(self.driver)
        urgent.checkSubmitButtonisclickable().click()
        #common.verifyPrimaryMemberName()
        member = Multimember(self.driver)
        member.getDropdownDownArow().click()
        time.sleep(2)
        Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
        print(Name_selectedMemeber)
        member.selectCloseDDButton().click()
        service = SelectServiceClinic(self.driver)
        bydefault_member = service.primarySelectMemberForTreatmentDDforMultiselctValue().text
        print(bydefault_member)
        assert (bydefault_member in Name_selectedMemeber)
        service.getSubmitButtonAtSelectSelection().click()
        #service.getSubmitButtonatSelectSelection().click()
        service = SelectServiceClinic(self.driver)
        text_selected = service.getBydefaultSelectedValueInDD().text
        print(text_selected)
        basepage = BaseClass(self.driver)
        basepage.ScrollDowntoPage()
        defaultClinic = service.getNY_BydefaultselectedClinic().click()
        self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
        common.GetAllVailableDatesSlots()
        service.getSubmitButtonAtSelectSelection().click()
        common.getAlluserDetailConfData()
        Header_text = vaccination.getInClinicPreventiveHeaderTextForSchedulingText().text
        assert (Header_text == "Review Appointment Details")
        app = AppointmentDetails(self.driver)
        app.getConfirmationButton().click()
        time.sleep(2)
        app.getAppointConfirmationPageLoaded()

    @allure.title("In clinic Vaccination Care-Verify Member is able to book an appointment for dependant by Changing clinic")
    def test_InClinic_Vaccination_VerifyNewRequestSubmissionForDependantByChangingClinic(self):
        home = HomePage(self.driver)
        home.getHomePageLogo().click()
        vaccination = InClinic_Vaccination(self.driver)
        common = CommonMethod(self.driver)
        time.sleep(5)
        common.navigateToScheduleAppointment()
        time.sleep(2)
        vaccination.getInClinicVaccinationLink().click()
        common.getAppointmentConfirmPopup()
        common.getVaccinationListUnderVaccinationModule().click()
        urgent = UrgentCare(self.driver)
        urgent.checkSubmitButtonisclickable().click()
        member = Multimember(self.driver)
        service = SelectServiceClinic(self.driver)
        service.getDownArrowWhenNoMemberSelectedInMemberDropdown().click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[3]").click()
        service.getSubmitButtonAtSelectSelection().click()
        time.sleep(5)
        service = SelectServiceClinic(self.driver)
        text_selected = service.getBydefaultSelectedValueInDD().text
        print(text_selected)
        basepage = BaseClass(self.driver)
        basepage.ScrollDowntoPage()
        defaultClinic = service.getNY_BydefaultselectedClinic().click()
        self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
        common.GetAllVailableDatesSlots()
        service.getSubmitButtonAtSelectSelection().click()
        common.GetAllVailableDatesSlots()
        service.getSubmitButtonAtSelectSelection().click()
        common.getAlluserDetailConfData()
        Header_text = vaccination.getInClinicPreventiveHeaderTextForSchedulingText().text
        assert (Header_text == "Review Appointment Details")
        app = AppointmentDetails(self.driver)
        app.getConfirmationButton().click()
        time.sleep(2)
        app.getAppointConfirmationPageLoaded()

    @allure.title("In clinic Vaccination Care-Verify Member is able to book an appointment for self by changing state and Clinic")
    def test_InClinic_VaccinationCare_VerifyNewRequestSubmissionForSelfByChangingStateAndClinic(self):
        home = HomePage(self.driver)
        home.getHomePageLogo().click()
        vaccination = InClinic_Vaccination(self.driver)
        common = CommonMethod(self.driver)
        common.navigateToScheduleAppointment()
        time.sleep(2)
        vaccination.getInClinicVaccinationLink().click()
        common.getAppointmentConfirmPopup()
        common.getVaccinationListUnderVaccinationModule().click()
        urgent = UrgentCare(self.driver)
        urgent.checkSubmitButtonisclickable().click()
        common.verifyPrimaryMemberNameForSingleSelect()
        service = SelectServiceClinic(self.driver)
        service.getBydefaultSelectedValueInDD().click()
        self.driver.find_element(By.XPATH, "//div[contains(@id,'-option-0')]").click()
        service.getOther_BydefaultSelectedClinic().click()
        self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
        schedule = ScheduleAppClinic(self.driver)
        flag = schedule.getFirstRadioButtonUnderAvailableSlot().is_selected
        assert (flag == True)
        service.getSubmitButtonAtSelectSelection().click()
        common.GetAllVailableDatesSlots()
        service.getSubmitButtonAtSelectSelection().click()
        common.getAlluserDetailConfData()
        Header_text = vaccination.getInClinicPreventiveHeaderTextForSchedulingText().text
        assert (Header_text == "Review Appointment Details")
        app = AppointmentDetails(self.driver)
        app.getConfirmationButton().click()
        time.sleep(2)
        app.getAppointConfirmationPageLoaded()

    @allure.title("Verify Member is able to book an appointment for dependant by changing State and Clinic")
    def test_InClinic_Vaccination_VerifyNewRequestSubmissionForDependantByChangingStateAndClinic(self):
        home = HomePage(self.driver)
        home.getHomePageLogo().click()
        vaccination = InClinic_Vaccination(self.driver)
        common = CommonMethod(self.driver)
        time.sleep(5)
        common.navigateToScheduleAppointment()
        time.sleep(2)
        vaccination.getInClinicVaccinationLink().click()
        common.getAppointmentConfirmPopup()
        common.getVaccinationListUnderVaccinationModule().click()
        urgent = UrgentCare(self.driver)
        urgent.checkSubmitButtonisclickable().click()
        member = Multimember(self.driver)
        service = SelectServiceClinic(self.driver)
        service.getDownArrowWhenNoMemberSelectedInMemberDropdown().click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[3]").click()
        service.getSubmitButtonAtSelectSelection().click()
        service.getBydefaultSelectedValueInDD().click()
        self.driver.find_element(By.XPATH, "//div[contains(@id,'-option-0')]").click()
        service.getOther_BydefaultSelectedClinic().click()
        self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
        schedule = ScheduleAppClinic(self.driver)
        flag = schedule.getFirstRadioButtonUnderAvailableSlot().is_selected
        assert (flag == True)
        service.getSubmitButtonAtSelectSelection().click()
        common.getAlluserDetailConfData()
        Header_text = vaccination.getInClinicPreventiveHeaderTextForSchedulingText().text
        assert (Header_text == "Review Appointment Details")
        app = AppointmentDetails(self.driver)
        app.getConfirmationButton().click()
        time.sleep(2)
        app.getAppointConfirmationPageLoaded()













