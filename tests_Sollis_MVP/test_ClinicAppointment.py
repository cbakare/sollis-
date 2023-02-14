import time
from datetime import date
import pytest
from allure_commons.types import AttachmentType
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.AppointmentConfDetails import AppointmentDetails
from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
from PageObject.Multimember import Multimember
from PageObject.ScheduleAppClinic import ScheduleAppClinic
from PageObject.SelectServiceClinic import SelectServiceClinic
from tests_Sollis_MVP.test_loginpage import Test_one
from utility.BaseClass import BaseClass
from utility.ScheduleCommonMethods import CommonMethod


@pytest.mark.usefixtures("setup")
class ClinicApp(CommonMethod, BaseClass):

    def test_VerifyClinicPrimeMemberNewAppointmentCreation(self, setup):
        try:
            log= self.logger()
            log.info("logging in")
            self.signin()
            log.info("login")
            self.Login()
            log.info("navigation")
            self.navigateToScheduleAppointment()
            time.sleep(5)
            log.info("scheduleApp")
            scheduleApp = ScheduleAppClinic(self.driver)
            scheduleApp.getCovidCarelinkclinic().click()
            self.getAppointmentConfirmPopup()
            time.sleep(10)
            self.getallVacinationlist()
            self.VaccineSelected()
            time.sleep(2)
            self.verifyallVaccinationOptions()
            self.verifyPrimaryMemberName()
            self.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            self.GetAllVailableDatesSlots()
            service=SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            self.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            detailConf.getConfirmationButton().click()
            #service.getSubmitButtonatSelectSelection().click()
            time.sleep(2)
        except Exception as E:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)




    def test_VerifyClinicAppForDependant(self):
        # base = BaseClass(self.driver)
        # base.signin()
        # base.Login()
        home=HomePage(self.driver)
        home.getHomePageLogo()
        time.sleep(5)
        scheduleApp = ScheduleAppClinic(self.driver)
        time.sleep(2)
        scheduleApp.NavigateToScheduleAppointmentPage().click()
        header = scheduleApp.headerInClinic().text
        if (header == "In-Clinic"):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(5)
        scheduleApp.getCovidCarelinkclinic().click()
        time.sleep(10)
        scheduleApp.getAppConfirmPopup()
        time.sleep(5)
        title = scheduleApp.getAppConfirmPopup().text
        print(title)
        # assert(title=="In Clinic Scheduling  Have you been diagnosed or exposed to Covid-19 in the last 14 days?")
        scheduleApp.getAppConfPopupYesButton().click()
        service = SelectServiceClinic(self.driver)
        time.sleep(5)
        selected_RB = service.getCovidTestingRadio().text
        service.getCovidTestingRadio().click()
        Act_selected_RB = service.selectedOptionforCovidtest().text
        if (selected_RB == Act_selected_RB):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
            assert False
        service.getSubmitButton().click()
        member = Multimember(self.driver)
        member.getDropdownDownArow().click()
        Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
        print(Name_selectedMemeber)
        dependant_name=member.getSecondDependantNameFromProfileDD().text
        print(dependant_name)
        member.selectCloseDDButton().click()
        service = SelectServiceClinic(self.driver)
        bydefault_tmember = service.primarySelectMemberForTreatmentDD().text
        print(bydefault_tmember)
        if (bydefault_tmember in Name_selectedMemeber):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1", attachment_type=AttachmentType.PNG)
            assert False
        service.getMemberDDDownArrow().click()
        service.getCrossMarkOfDDForSelf().click()
        self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
        service.getSubmitButton().click()
        text_selected = service.getBydefaultSelectedValueInDD().text
        print(text_selected)
        if (text_selected == "NY"):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)
            assert False

        basepage = BaseClass(self.driver)
        basepage.ScrollDowntoPage()
        if text_selected == "NY":
            Ny_defaultClinic = service.getNY_BydefaultselectedClinic().text
            if ("Sollis UES" == Ny_defaultClinic):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1", attachment_type=AttachmentType.PNG)
                assert False

        else:
            Other_defaultClinic = service.getOther_BydefaultSelectedClinic().text
            print(Other_defaultClinic)
            assert ("Select Clinic" == Other_defaultClinic)
        text_Date = service.getdate_dayforschedilingInclinic().text
        # print(text_Date)
        Todays_date = date.today()
        Day = Todays_date.strftime("%A")
        print(Day)
        if Day == "Friday" or "Saturday" or "Sunday":
            Day_status = "Fri" or "Sat" or "Sun" not in text_Date
            assert (text_Date != "Fri" or "Sat" or "Sun")
        slots_1 = service.getAllAvailableslots()
        Available_slots = []
        for slot in slots_1:
            Slots2 = slot.text
            Available_slots.append(Slots2)
        # print(Available_slots)
        service.getSubmitButtonAtSelectSelection().click()
        time.sleep(2)
        detailConf = AppointmentDetails(self.driver)
        dict1 = {}
        headers_list_1 = detailConf.getAllheaders()
        headers_list = []
        detailConf_List = []
        Userdata_list = detailConf.getUserDataUnderheader()
        for header in headers_list_1:
            Label = header.text
            print(Label)
            headers_list.append(Label)
        print(headers_list)
        for data in Userdata_list:
            user_data = data.text
            print(user_data)
            detailConf_List.append(user_data)
        detailConf_List.pop()
        detailConf_List.append(detailConf.getPrefferedTime().text)
        print(detailConf_List)
        dict1 = dict(zip(headers_list, detailConf_List))
        detailConf.getConfirmationButton().click()




