import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from PageObject.Billings import Billings
from PageObject.HomePage import HomePage
from PageObject.Multimember import Multimember
from utility.BaseClass import BaseClass
from utility.ScheduleCommonMethods import CommonMethod


@pytest.mark.usefixtures("setup")
class Test_Billings():
    @allure.title("Verify total unread Billing count for primary member")
    def test_VerifyUnreadCountForBillings(self,setup,LoginpageDataloader):
        try:
            base = BaseClass(self.driver)
            base.signin(setup)
            base.Login(LoginpageDataloader)
            bills=Billings(self.driver)
            time.sleep(2)
            base.ScrollDowntoPage()
            homePage_unreadCountLable=self.driver.find_elements(By.XPATH,"//p[text()='Billing']//following::span")
            element_Visibility_test=len(homePage_unreadCountLable)
            if element_Visibility_test!= 0:
                unread_Count_HomePage=bills.getUnreadBillingCount().text
                print(unread_Count_HomePage)
            else:
                print("No Unread bills are present")
               #add Db query
        except TimeoutError as e:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",attachment_type=AttachmentType.PNG)

    @allure.title("Verify total Billing count for primary member")
    def test_verifyTotalCaountforBillings(self):
        # base = BaseClass(self.driver)
        # base.signin(setup)
        # base.Login()
        try:
            home=HomePage(self.driver)
            home.getHomePageLogo().click()
            time.sleep(10)
            bills = Billings(self.driver)
            bills.getBillingHomePageLink().click()
            Page_header=bills.getBillingHeaderAtBillingPage().text
            assert(Page_header=="Billing")
            Column_header1=bills.getBillingColumnheader_Date().text
            assert(Column_header1=="DATE")
            Column_header2=bills.getBillingColumnheader_Filename().text
            assert(Column_header2=="FILE NAME")
            Table_Record_count=len(bills.getBillingColumnheaders())
            print(Table_Record_count)
            #add DB query
        except TimeoutError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Appointment1",
                          attachment_type=AttachmentType.PNG)

    @allure.title("Verify total unread Billing count by selecting dependant from the member list")
    def test_VerifyUnreadCountIsGettingUpdatedOnSelectionOfMember(self):
        home = HomePage(self.driver)
        home.getHomePageLogo().click()
        bills = Billings(self.driver)
        time.sleep(2)
        base=BaseClass(self.driver)
        base.ScrollDowntoPage()
        homePage_unreadCountLable = self.driver.find_elements(By.XPATH, "//p[text()='Billing']//following::span")
        element_Visibility_test = len(homePage_unreadCountLable)
        if element_Visibility_test != 0:
            unread_Count_HomePage = bills.getUnreadBillingCount().text
            print(unread_Count_HomePage)
        else:
            print("No Unread bills are present")
            unread_Count_HomePage=0
        member=Multimember(self.driver)
        member.getDropdownDownArow().click()
        common = CommonMethod(self.driver)
        common.updateTheDependantFromMemberDropdown()
        homePage_unreadCountLable = self.driver.find_elements(By.XPATH, "//p[text()='Billing']//following::span")
        element_Visibility_test = len(homePage_unreadCountLable)
        if element_Visibility_test !=0 :
            unread_Count_HomePage_updated = bills.getUnreadBillingCount().text
            print(unread_Count_HomePage_updated)
            assert(unread_Count_HomePage_updated>=unread_Count_HomePage)
        else :
            print("No Unread bills are present")
        member.getDropdownDownArow().click()
        common.unselectTheDependant()









