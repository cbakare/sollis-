from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Messeges():
    def __init__(self,driver):
        self.driver=driver

    def getHomePagePrimaryMemberInitials(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//span/span")))

    def getHomePageMessageLink(self):
        return  WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Messages']")))

    def getMassagesPageHeader(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//h4[contains(text(),'Messages')]")))

    def getMessageTotalCount(self):
        return  self.driver.find_elements(By.XPATH,"//div[@class='tab-pane active']/div[3]/div/form/div")

    def getTextMessageNorecordsAvailble(self):
        return  WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='tab-pane active']//p[@class='mt-3'][normalize-space()='No new mail']")))

    def getComposeButton(self):
        return  WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//a[contains(@class,'button-action btn-light')]")))

    def getSentLinkOnMessagePage(self):
        return   WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//p[normalize-space()='Sent']")))

    def getNoRecordMessageforSent(self):
        return  WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='tab-pane active']//p[@class='mt-3'][normalize-space()='No Sent mail']")))

    def getDeleteLinkOnMessagePage(self):
        return  WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//p[normalize-space()='Deleted']")))



