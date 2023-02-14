import datetime
import random
import time
from datetime import date


import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.AppointmentConfDetails import AppointmentDetails
from PageObject.HouseCallCovidcare import HouseCallCovidCare
from PageObject.VaccinationClinic import InClinic_Vaccination
from PageObject.Multimember import Multimember
from PageObject.ScheduleAppClinic import ScheduleAppClinic
from PageObject.SelectServiceClinic import SelectServiceClinic
from PageObject.UrgentCareInClinic import UrgentCare
from utility.BaseClass import BaseClass


class CommonMethod(BaseClass):

    # def __init__(self, driver):
    #     self.driver = driver



    def getAppointmentConfirmPopup(self):
        scheduleApp = ScheduleAppClinic(self.driver)
        scheduleApp.getAppConfirmPopup()
        time.sleep(2)
        title = scheduleApp.getAppConfirmPopup().text
        print(title)
        # assert(title=="In Clinic Scheduling  Have you been diagnosed or exposed to Covid-19 in the last 14 days?")
        scheduleApp.getAppConfPopupYesButton().click()

    def appointmentConfirmPopupWithNoOption(self):
        scheduleApp = ScheduleAppClinic(self.driver)
        scheduleApp.getAppConfirmPopup()
        time.sleep(5)
        title = scheduleApp.getAppConfirmPopup().text
        print(title)
        scheduleApp.getAppConfPopupNoButton().click()



    def verifySelectServiceclinicPageCovidTesting(self):
        service = SelectServiceClinic(self.driver)
        time.sleep(5)
        selected_RB = service.getCovidTestingRadio().text
        service.getCovidTestingRadio().click()
        Act_selected_RB = service.selectedOptionforCovidtest().text
        assert (selected_RB == Act_selected_RB)

    def getAllVacinationlist(self):
        service = SelectServiceClinic(self.driver)
        #base = BaseClass(self.driver)
        self.ScrollDowntoPage()
        service.getCovidVaccinationHeader().click()
        time.sleep(2)
        VaccinatioList = []
        VaccinationNames = []
        VaccinatioList = service.getAllCovidVaccinations()
        for vaccination in VaccinatioList:
            Name = vaccination.text
            print(Name)
            VaccinationNames.append(Name)

    def verifyPrimaryMemberNameForSingleSelect(self):
        time.sleep(2)
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
        # time.sleep(2)


    def verifyPrimaryMemberName(self):
        time.sleep(2)
        member = Multimember(self.driver)
        member.getDropdownDownArow().click()
        time.sleep(2)
        Name_selectedMemeber = member.SelectedPrimaryMemeberhome().text
        print(Name_selectedMemeber)
        member.selectCloseDDButton().click()
        service = SelectServiceClinic(self.driver)
        bydefault_member = service.primarySelectMemberForTreatmentDD().text
        print(bydefault_member)
        assert (bydefault_member in Name_selectedMemeber)
        service.getSubmitButtonAtSelectSelection().click()
        # time.sleep(2)

    def AddDependantName(self):
        time.sleep(2)
        member = Multimember(self.driver)
        member.getDropdownDownArow().click()
        service=SelectServiceClinic(self.driver)
        service.getCrossMarkOfDDForSelf().click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class=' css-b62m3t-container']/div[2]/div/div[2]").click()
        service.getSubmitButton().click()



    def navigateToScheduleAppointment(self):
        scheduleApp = ScheduleAppClinic(self.driver)
        time.sleep(5)
        scheduleApp.NavigateToScheduleAppointmentPage().click()
        header = scheduleApp.headerInClinic().text
        assert (header == "In-Clinic")

    def getListofPrimarySynptomps(self):
        urgentCare=UrgentCare(self.driver)
        symptoms=urgentCare.getListForAllprimarySymtoms()
        Allsymptopmlist=[]
        for symptom in symptoms:
            N_symptoms=symptom.text
            Allsymptopmlist.append(N_symptoms)
        print(Allsymptopmlist)
        return  Allsymptopmlist

    def verify_Bydefault_userLocation_slots_clinic_for_vaccinaton(self,UserLocation):
        common=CommonMethod(self.driver)
        common.waitUntilLoadIframe()
        service = SelectServiceClinic(self.driver)
        text_selected= service.getBydefaultSelectedState().text
        print(text_selected)
        self.ScrollDowntoPage()
        if text_selected == UserLocation:
            defaultClinic = service.getNY_BydefaultselectedClinic().text
        else:
            Other_defaultClinic = service.getOther_BydefaultSelectedClinic().text
            print(Other_defaultClinic)

    def GetAllVailableDatesSlots(self):
        service=SelectServiceClinic(self.driver)
        text_Date = service.getdate_dayforschedilingInclinic().text
        print(text_Date)
        Todays_date=datetime.date.today()
        Day = Todays_date.strftime("%A")
        slots_1 = service.getAllAvailableslots()
        Available_slots = []
        for slot in slots_1:
            Slots2 = slot.text
            Available_slots.append(Slots2)

    def getAlluserDetailConfData(self):
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
            detailConf_List.append(user_data)
        detailConf_List.pop()
        #detailConf_List.append(detailConf.getPrefferedTime().text)
        print(detailConf_List)
        dict1 = dict(zip(headers_list, detailConf_List))

    def getAllUserdataintoListforHouseCall(self):
        time.sleep(2)
        detailConf = AppointmentDetails(self.driver)
        dict1 = {}
        headers_list_1 = detailConf.getAllheaders()
        headers_list = []
        for header in headers_list_1:
            Label = header.text
            headers_list.append(Label)
        print(headers_list)
        userdata_list=[]
        userdata=AppointmentDetails(self.driver)
        userdata_list.append(userdata.getValueforRequestForHeader().text)
        userdata_list.append(userdata.getValueForMemberAttendingAppointment().text)
        userdata_list.append(userdata.getValueForHouseCallAddress().text)
        userdata_list.append(userdata.getValueForSpecialInstruction().text)
        userdata_list.append(userdata.getValueForPhoneNumber().text)
        userdata_list.append(userdata.getValuePreffereTime().text)
        print(userdata_list)
        dict1 = dict(zip(headers_list, userdata_list))
        print(dict1)

    def getallVacinationlist(self):
        service = SelectServiceClinic(self.driver)
        #base = BaseClass(self.driver)
        time.sleep(2)
        self.ScrollDowntoPage()
        service.getCovidVaccinationHeader().click()
        time.sleep(2)
        VaccinatioList = []
        VaccinationNames = []
        VaccinatioList = service.getAllCovidVaccinations()
        for vaccination in VaccinatioList:
            Name = vaccination.text
            print(Name)
            VaccinationNames.append(Name)

    def VaccineSelected(self):
        service = SelectServiceClinic(self.driver)
        service.getRadioButton().click()
        Act_selected_vaccin = service.getRadioButton().text
        print(Act_selected_vaccin)
        selected_vaccin = service.selectedOptionForCovidVaccine().text
        if (Act_selected_vaccin == selected_vaccin):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          ttachment_type=AttachmentType.PNG)
            assert False

    def verifyallVaccinationOptions(self):
        service = SelectServiceClinic(self.driver)
        Act_selected_vaccine = service.getRadioButton().text
        pFizer = service.getAllOptionsforpFizer()
        pFizerOptionList = []
        for option in pFizer:
            pFizerOptions = option.text
            pFizerOptionList.append(pFizerOptions)
        service.getFirstOptionUnderPfizer().click()
        time.sleep(2)
        Pfizer_radioB = service.getFirstOptionUnderPfizer().text
        if (Pfizer_radioB in pFizerOptionList):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)
            assert False
        selected_vaccination_str = Act_selected_vaccine + ', ' + Pfizer_radioB
        Actual_selected_Vaccination_dose = service.getSelectedStringVaccination().text
        if (selected_vaccination_str == Actual_selected_Vaccination_dose):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          ttachment_type=AttachmentType.PNG)
            assert False
        service.getSubmitButton().click()

    def NavigatetoHousCallTab(self):
        housecall=HouseCallCovidCare(self.driver)
        housecall.getHouseCallHeaderLink().click()
        time.sleep(2)
    def VerifyHouseCallHeader(self):
        housecall = HouseCallCovidCare(self.driver)
        HouseCallHeader=housecall.getHeaderHouseCall().text
        assert(HouseCallHeader=="House Call")

    def NavigateToHouseCallCovidCare(self):
        housecall = HouseCallCovidCare(self.driver)
        housecall.getHouseCallGetCovidCareOption().click()
        time.sleep(2)
    def VerifyRequestHouseCallHeader(self):
        housecall = HouseCallCovidCare(self.driver)
        housecall.getRequestAddressforHoueCallHeader()

    def houseCallPrimaryRequestaddress(self):
        housecall = HouseCallCovidCare(self.driver)
        housecall.getPrimeMemberAddressForHouseCall().click()
        time.sleep(2)

    def houseCallSpecialInstruction(self):
        housecall = HouseCallCovidCare(self.driver)
        housecall.getAlternetAdressSpecialInstruction().send_keys("Adm_test")

    def HouseCallrequestLoadingPhoneNumberAndPrefferedTiming(self):
        housecall = HouseCallCovidCare(self.driver)
        housecall.getPrefferedPhoneLabel().is_displayed()
        housecall.getPhoneNuber().is_displayed()
        housecall.getASAPradioButton().click()

    def updateTheDependantFromMemberDropdown(self):
        member=Multimember(self.driver)
        list1 = member.getcheckboxesForMemberDropdown()
        for checkbox in list1:
            Status_checkbox = checkbox.is_selected()
            print(Status_checkbox)
            if Status_checkbox == False:
                checkbox.click()
                break
        member.getUpdateButtoninMemberDropdown().click()

    def unselectTheDependant(self):
        member = Multimember(self.driver)
        list1 = member.getcheckboxesForMemberDropdown()
        for checkbox in list1:
            if checkbox.is_selected():
                print(list1)
                index=list1.index(checkbox)
                if index!=0:
                    checkbox.click()
                    break
        member.getUpdateButtoninMemberDropdown().click()

    def enterDetailForAlternetaddress(self):
        housecare = HouseCallCovidCare(self.driver)
        housecare.getAlternetAddressField().send_keys("adm test")
        housecare.getAlternetAddressAppartment().send_keys("Sollis Adm Test")
        housecare.getAlternetAddressCity().send_keys("Adm City")
        housecare.getAlternetAddressState().click()
        housecare.enterAleternetAddressState().send_keys("Newyork")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[contains(@class,'css-26l3')]/div/div[text()='NewYork']").click()
        housecare.getAlternetAddressZipCode().send_keys('123456')
        housecare.getAlternetAdressSpecialInstruction().send_keys("test offshore automation")

    def getAllVaccinationList(self):
        service= SelectServiceClinic(self.driver)
        service.openCovidVaccinationListAtSelectServicePage().click()
        listVaccination=service.getAllVaccinationListUnderSelectServicePage()
        Vaccinations_Available=[]
        for vaccine in listVaccination:
            Vacc=vaccine.text
            Vaccinations_Available.append(Vacc)
        print(Vaccinations_Available)

    def selectvaccinationRandomly(self):
        service = SelectServiceClinic(self.driver)
        service.openCovidVaccinationListAtSelectServicePage()
        listVaccination = service.getAllVaccinationListUnderSelectServicePage()
        return random.choice(listVaccination)


    def getAlldosesforSelectedVaccine(self):
        service = SelectServiceClinic(self.driver)
        Available_doses=service.getDosesUnderTheVaccination()
        return  random.choice(Available_doses)

    def navigateToVaccination(self):
        vaccination=InClinic_Vaccination(self.driver)
        vaccination.getInClinicVaccinationLink()

    def getVaccinationListUnderVaccinationModule(self):
       vaccination=InClinic_Vaccination(self.driver)
       List=vaccination.getListOfAllVaccinationUnderSelectVaccination()
       return random.choice(List)

    def getCovidVaccinationLinkAtselectServicePage(self):
        service=SelectServiceClinic(self.driver)
        service.openCovidVaccinationListAtSelectServicePage().click()


    def selectCovidTreatementOptionRandomly(self):
        house=HouseCallCovidCare(self.driver)
        house.openCovidTreatmentTabUnderSelectService().click()
        List_radio=house.getAllRadioButtonUnderCovidtreatment()
        return random.choice(List_radio)

    def waitUntilLoadIframe(self):
        self.driver.implicitly_wait(15)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//iframe[@title='map']")))
        Flag=WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//iframe[@title='map']"))).is_displayed()
        print(Flag)
        if Flag==False:
            self.driver.refresh()
            self.driver.implicitly_wait(10)






























