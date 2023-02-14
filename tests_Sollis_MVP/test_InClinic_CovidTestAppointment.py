import time
from datetime import date

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from PageObject.AppointmentConfDetails import AppointmentDetails
from PageObject.HomePage import HomePage
from PageObject.Multimember import Multimember
from PageObject.ScheduleAppClinic import ScheduleAppClinic
from PageObject.SelectServiceClinic import SelectServiceClinic
from utility.BaseClass import BaseClass
from utility.ScheduleCommonMethods import CommonMethod


@pytest.mark.usefixtures("setup")
class Test_InClinicCovidTestAppointment():
    @allure.title("In Clinic-Verify Prime member is able to submit the request for the Covid test")
    def test_InClinicCovidCare_VerifyAppointmentCreationForCovidTestForPrimeMember(self, setup, LoginpageDataloader):
        #try:
            base = BaseClass(self.driver)
            base.signin(setup)
            base.Login(LoginpageDataloader)
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
            scheduleApp.getCovidCarelinkclinic().click()
            common = CommonMethod(self.driver)
            common.getAppointmentConfirmPopup()
            service = SelectServiceClinic(self.driver)
            common.verifySelectServiceclinicPageCovidTesting()
            service.getSubmitButtonAtSelectSelection().click()
            common.verifyPrimaryMemberName()
            common.verify_Bydefault_userLocation_slots_clinic_for_vaccinaton("NY")
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            time.sleep(2)
            common.getAlluserDetailConfData()
            detailConf = AppointmentDetails(self.driver)
            dict1 = {}
            headers_list_1 = detailConf.getAllheaders()
            headers_list = []
            detailConf_List = []
            Userdata_list = detailConf.getUserDataUnderheader()
            detailConf.getConfirmationButton().click()
            time.sleep(5)
            flag = detailConf.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)


    @allure.title("In Clinic-Verify Prime member is able to create request for Dependant for Covid test")
    def test_InClinicCovidCare_VerifyAppointmentCreationForDependantForCovidTest(self):
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(5)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            header = scheduleApp.headerInClinic().text
            if (header == "In-Clinic"):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            #time.sleep(2)
            scheduleApp.getCovidCarelinkclinic().click()
            common = CommonMethod(self.driver)
            common.getAppointmentConfirmPopup()
            service = SelectServiceClinic(self.driver)
            common.verifySelectServiceclinicPageCovidTesting()
            service.getSubmitButtonAtSelectSelection().click()
            member = Multimember(self.driver)
            member.getDropdownDownArow().click()
            Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
            print(Name_selectedMemeber)
            dependant_name_1 = member.getSecondDependantNameFromProfileDD().text
            dependant_name_2 = dependant_name_1.rsplit(" (")
            dependant_name = dependant_name_2[0]
            print(dependant_name)
            member.selectCloseDDButton().click()
            service = SelectServiceClinic(self.driver)
            bydefault_tmember = service.primarySelectMemberForTreatmentDD().text
            print(bydefault_tmember)
            if (bydefault_tmember in Name_selectedMemeber):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            service.getCrossMarkForSelectedMember().click()
            service.getDownArrowWhenNoMemberSelectedInMemberDropdown().click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            service.getSubmitButtonAtSelectSelection().click()
            text_selected = service.getBydefaultSelectedValueInDD().text
            print(text_selected)
            if (text_selected == "NY"):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False

            basepage = BaseClass(self.driver)
            basepage.ScrollDowntoPage()
            if text_selected == "NY":
                Ny_defaultClinic = service.getNY_BydefaultselectedClinic().text
                print(Ny_defaultClinic)
                time.sleep(2)
            else:
                Other_defaultClinic = service.getOther_BydefaultSelectedClinic().text
                print(Other_defaultClinic)
                assert ("Select Clinic" == Other_defaultClinic)
            common.GetAllVailableDatesSlots()
            service.getSubmitButtonAtSelectSelection().click()
            time.sleep(2)
            detailConf = AppointmentDetails(self.driver)
            common.getAlluserDetailConfData()
            time.sleep(5)
            flag = detailConf.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)

    @allure.title(
        "In Clinic-Verify user is able to create the appointment request for self and dependant for the Covid test")
    def test_InClinic_VerifyAppointmentCreationForDependantandPrimeMemberforCovidTest(self):
        # try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(5)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            header = scheduleApp.headerInClinic().text
            if (header == "In-Clinic"):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            scheduleApp.getCovidCarelinkclinic().click()
            scheduleApp.getAppConfirmPopup()
            # title = scheduleApp.getAppConfirmPopup().text
            title = scheduleApp.getAppConfirmPopup().text
            scheduleApp.getAppConfPopupYesButton().click()
            service = SelectServiceClinic(self.driver)
            time.sleep(2)
            selected_RB = service.getCovidTestingRadio().text
            service.getCovidTestingRadio().click()
            Act_selected_RB = service.selectedOptionforCovidtest().text
            if (selected_RB == Act_selected_RB):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            service.getSubmitButtonAtSelectSelection().click()
            member = Multimember(self.driver)
            member.getDropdownDownArow().click()
            Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
            print(Name_selectedMemeber)
            dependant_name_1 = member.getSecondDependantNameFromProfileDD().text
            dependant_name_2 = dependant_name_1.rsplit(" (")
            dependant_name = dependant_name_2[0]
            print(dependant_name)
            member.selectCloseDDButton().click()
            service = SelectServiceClinic(self.driver)
            bydefault_member = service.primarySelectMemberForTreatmentDD().text
            print(bydefault_member)
            if (bydefault_member in Name_selectedMemeber):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            service.ClickOnTheDropdownForMember().click()
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            time.sleep(2)
            service.getSubmitButtonAtSelectSelection().click()
            time.sleep(5)
            text_selected = service.getBydefaultSelectedValueInDD().text
            if text_selected == "NY":
                Ny_defaultClinic = service.getNY_BydefaultselectedClinic().text
                print(Ny_defaultClinic)
            else:
                Other_defaultClinic = service.getOther_BydefaultSelectedClinic().text
                print(Other_defaultClinic)
            text_Date = service.getdate_dayforschedilingInclinic().text
            Todays_date = date.today()
            Day = Todays_date.strftime("%A")
            print(Day)
            slots_1 = service.getAllAvailableslots()
            Available_slots = []
            for slot in slots_1:
                Slots2 = slot.text
                Available_slots.append(Slots2)
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
            print(detailConf_List)
            dict1 = dict(zip(headers_list, detailConf_List))
            time.sleep(2)
            detailConf.getConfirmationButton().click()
            flag = detailConf.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
        # except TimeoutError as e:
        #     allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
        #                   attachment_type=AttachmentType.PNG)

    @allure.title(
        "In Clinic-Covid Test-Verify user is able to create appointment request for self for default state but by changing Clinic")
    def test_InClinicCovidCare_VerifyAppointmentCreationForCovidTestForPrimeMemberDefaultLocationAndChangingClinic(
            self):
       #try:
            home = HomePage(self.driver)
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
            scheduleApp.getCovidCarelinkclinic().click()
            common = CommonMethod(self.driver)
            common.getAppointmentConfirmPopup()
            service = SelectServiceClinic(self.driver)
            time.sleep(2)
            selected_RB = service.getCovidTestingRadio().text
            service.getCovidTestingRadio().click()
            Act_selected_RB = service.selectedOptionforCovidtest().text
            if (selected_RB == Act_selected_RB):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            service.getSubmitButtonAtSelectSelection().click()
            common.verifyPrimaryMemberName()
            text_selected = service.getBydefaultSelectedValueInDD().text
            print(text_selected)
            basepage = BaseClass(self.driver)
            basepage.ScrollDowntoPage()
            defaultClinic = service.getNY_BydefaultselectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
            text_Date = service.getdate_dayforschedilingInclinic().text
            Todays_date = date.today()
            Day = Todays_date.strftime("%A")
            print(Day)
            slots_1 = service.getAllAvailableslots()
            Available_slots = []
            for slot in slots_1:
                Slots2 = slot.text
                Available_slots.append(Slots2)
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
            print(detailConf_List)
            dict1 = dict(zip(headers_list, detailConf_List))
            detailConf.getConfirmationButton().click()
            flag = detailConf.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
        # except TimeoutError as e:
        #     allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
        #                   attachment_type=AttachmentType.PNG)

    @allure.title(
        "In Clinic-Covid Test-Verify Prime Member is able to create clinic appointment by changing state and Clinic")
    def test_InClinicCovidCare_VerifyAppointmentCreationForCovidTestForPrimeMemberbyChangeStateAndChangeClinic(self,setup):
        try:
            # base = BaseClass(self.driver)
            # base.signin(setup)
            # base.Login()
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            time.sleep(2)
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            schedule = ScheduleAppClinic(self.driver)
            schedule.getCovidCarelinkclinic().click()
            common.getAppointmentConfirmPopup()
            common.verifySelectServiceclinicPageCovidTesting()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            common.verifyPrimaryMemberName()
            self.driver.refresh()
            time.sleep(20)
            base=BaseClass(self.driver)
            # base.ScrollDowntoPage()
            service.getBydefaultSelectedValueInDD().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'-option-0')]").click()
            service.getOther_BydefaultSelectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
            flag = schedule.getFirstRadioButtonUnderAvailableSlot().is_selected
            assert (flag == True)
            service.getSubmitButtonAtSelectSelection().click()
            common.getAlluserDetailConfData()
            appointmentDetail = AppointmentDetails(self.driver)
            appointmentDetail.getConfirmationButton().click()
            flag = appointmentDetail.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)

        except TimeoutError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    @allure.title("verify prime member can create an appointment for self and dependant by changing clinic ")
    def test_InClinicCovidCare_AppointmentCreationForCovidTestForPrimeMemberAndDependantByChangingChangeClinic(self):
        #try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            time.sleep(2)
            common = CommonMethod(self.driver)
            common.navigateToScheduleAppointment()
            schedule = ScheduleAppClinic(self.driver)
            schedule.getCovidCarelinkclinic().click()
            common.getAppointmentConfirmPopup()
            common.verifySelectServiceclinicPageCovidTesting()
            service = SelectServiceClinic(self.driver)
            service.getSubmitButtonAtSelectSelection().click()
            service = SelectServiceClinic(self.driver)
            time.sleep(2)
            common.verifySelectServiceclinicPageCovidTesting()
            service.getSubmitButtonAtSelectSelection().click()
            member = Multimember(self.driver)
            member.getDropdownDownArow().click()
            Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
            print(Name_selectedMemeber)
            dependant_name_1 = member.getSecondDependantNameFromProfileDD().text
            dependant_name_2 = dependant_name_1.rsplit(" (")
            dependant_name = dependant_name_2[0]
            print(dependant_name)
            member.selectCloseDDButton().click()
            service = SelectServiceClinic(self.driver)
            bydefault_member = service.primarySelectMemberForTreatmentDD().text
            print(bydefault_member)
            if (bydefault_member in Name_selectedMemeber):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            service.ClickOnTheDropdownForMember().click()
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            time.sleep(2)
            service.getSubmitButtonAtSelectSelection().click()
            text_selected = service.getBydefaultSelectedValueInDD().text
            print(text_selected)
            basepage = BaseClass(self.driver)
            basepage.ScrollDowntoPage()
            defaultClinic = service.getNY_BydefaultselectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
            schedule = ScheduleAppClinic(self.driver)
            flag = schedule.getFirstRadioButtonUnderAvailableSlot().is_selected
            assert (flag == True)
            service.getSubmitButtonAtSelectSelection().click()
            common = CommonMethod(self.driver)
            common.getAlluserDetailConfData()
            appointmentDetail = AppointmentDetails(self.driver)
            appointmentDetail.getConfirmationButton().click()
            flag = appointmentDetail.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)

        # except TimeoutError as e:
        #     allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
        #                   attachment_type=AttachmentType.PNG)

    @allure.title(
        "verify prime member can create an appointment for self and dependant by changing the State and clinic")
    def test_InClinic_VerifyAppointmentCreationForDependantandPrimeMemberforCovidTestbyChangingStateandClinic(self):
        #try:
            home = HomePage(self.driver)
            home.getHomePageLogo().click()
            scheduleApp = ScheduleAppClinic(self.driver)
            time.sleep(5)
            scheduleApp.NavigateToScheduleAppointmentPage().click()
            header = scheduleApp.headerInClinic().text
            if (header == "In-Clinic"):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            scheduleApp.getCovidCarelinkclinic().click()
            scheduleApp.getAppConfirmPopup()
            title = scheduleApp.getAppConfirmPopup().text
            print(title)
            scheduleApp.getAppConfPopupYesButton().click()
            service = SelectServiceClinic(self.driver)
            time.sleep(2)
            selected_RB = service.getCovidTestingRadio().text
            service.getCovidTestingRadio().click()
            Act_selected_RB = service.selectedOptionforCovidtest().text
            if (selected_RB == Act_selected_RB):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            service.getSubmitButtonAtSelectSelection().click()
            member = Multimember(self.driver)
            member.getDropdownDownArow().click()
            Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
            print(Name_selectedMemeber)
            dependant_name_1 = member.getSecondDependantNameFromProfileDD().text
            dependant_name_2 = dependant_name_1.rsplit(" (")
            dependant_name = dependant_name_2[0]
            print(dependant_name)
            member.selectCloseDDButton().click()
            service = SelectServiceClinic(self.driver)
            bydefault_member = service.primarySelectMemberForTreatmentDD().text
            print(bydefault_member)
            if (bydefault_member in Name_selectedMemeber):
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)
                assert False
            service.ClickOnTheDropdownForMember().click()
            self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
            time.sleep(2)
            service.getSubmitButtonAtSelectSelection().click()
            time.sleep(10)
            service.getBydefaultSelectedValueInDD().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'-option-0')]").click()
            service.getOther_BydefaultSelectedClinic().click()
            self.driver.find_element(By.XPATH, "//div[contains(@id,'option-1')]").click()
            schedule = ScheduleAppClinic(self.driver)
            flag = schedule.getFirstRadioButtonUnderAvailableSlot().is_selected
            assert (flag == True)
            service.getSubmitButtonAtSelectSelection().click()
            common = CommonMethod(self.driver)
            common.getAlluserDetailConfData()
            appointmentDetail = AppointmentDetails(self.driver)
            appointmentDetail.getConfirmationButton().click()
            flag = appointmentDetail.getAppointConfirmationPageLoaded().is_displayed()
            if flag == True:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                              attachment_type=AttachmentType.PNG)


        # except TimeoutError as e:
        #     allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
        #                   attachment_type=AttachmentType.PNG)
