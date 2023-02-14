import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.HomePage import HomePage
from PageObject.Messages import Messeges
from utility.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Test_Messages():
    def test_verifyMessagesCount(self,setup, LoginpageDataloader):
        base = BaseClass(self.driver)
        base.signin(setup)
        base.Login(LoginpageDataloader)
        msg = Messeges(self.driver)
        Login_Member_inn=msg.getHomePagePrimaryMemberInitials().text
        print(Login_Member_inn)
        msg.getHomePageMessageLink().click()
        Header_Menu_msg=msg.getMassagesPageHeader().text
        if(Header_Menu_msg=="Messages"):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Message1",attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(2)
        # Mssg_count_Logo=self.driver.find_elements(By.XPATH,"//div[contains(@class,'message-section')]")
        # Mssg_count=len(Mssg_count_Logo)
        # print(Mssg_count)
        home=HomePage(self.driver)
        home.getHomePageLogo().click()
        Home_MSg_count1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Messages']/span"))).text
        Home_MSg_count=int(Home_MSg_count1)
        print(Home_MSg_count1)
        # if(Mssg_count==Home_MSg_count1):
        #     assert True
        # else:
        #     allure.attach(self.driver.get_screenshot_as_png(), name="message2",attachment_type=AttachmentType.PNG)
        #     assert False

    def test_verifytotalMessagesUnderTheInbox(self):
        home=HomePage(self.driver)
        home.getHomePageLogo().click()
        msg=Messeges(self.driver)
        msg.getHomePageMessageLink().click()
        Header_Menu_msg=msg.getMassagesPageHeader().text
        if (Header_Menu_msg == "Messages"):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="message3",
                              attachment_type=AttachmentType.PNG)
            assert False
        TotalMsg=len(msg.getMessageTotalCount())
        Compose_button_flag= msg.getComposeButton().is_displayed()
        print(Compose_button_flag)
        print(TotalMsg)
        if TotalMsg==0:
            NoMessageavaialble_Message=msg.getTextMessageNorecordsAvailble().text
            print(NoMessageavaialble_Message)
            #verify exact message
        else:
            TotalInboxMsg=TotalMsg
            #assert with query

    def test_verifytotalMessagesUnderSent(self):
        home = HomePage(self.driver)
        home.getHomePageLogo().click()
        msg = Messeges(self.driver)
        msg.getHomePageMessageLink().click()
        Header_Menu_msg = msg.getMassagesPageHeader().text
        if (Header_Menu_msg == "Messages"):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="message4",
                                  attachment_type=AttachmentType.PNG)
            assert False
        msg.getSentLinkOnMessagePage().click()
        time.sleep(2)
        TotalMsg = len(msg.getMessageTotalCount())
        print(TotalMsg)
        if TotalMsg == 0:
            NoSentRecordMessage=msg.getNoRecordMessageforSent().text
            print(NoSentRecordMessage)
        else:
            Total_sent_message=TotalMsg
            #Vallidate across query

    def test_verifytotalMessagesUnderDelete(self):
        home = HomePage(self.driver)
        home.getHomePageLogo().click()
        msg = Messeges(self.driver)
        msg.getHomePageMessageLink().click()
        Header_Menu_msg = msg.getMassagesPageHeader().text
        if (Header_Menu_msg == "Messages"):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="message5",
                          attachment_type=AttachmentType.PNG)
            assert False
        msg.getDeleteLinkOnMessagePage().click()
        time.sleep(2)
        TotalMsg = len(msg.getMessageTotalCount())
        print(TotalMsg)
        if TotalMsg == 0:
            NoSentRecordMessage = msg.getNoRecordMessageforSent().text
            print(NoSentRecordMessage)
        else:
            Total_delete_Msg=TotalMsg
            #data base connection












