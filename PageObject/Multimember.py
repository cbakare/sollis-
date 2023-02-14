from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Multimember():

    def __init__(self, driver):
        self.driver = driver

    def getDropdownDownArow(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//i[@class='fa-light fa-chevron-down']")))

    def SelectedPrimaryMemeberhome(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='check1']//following::label[1]/span")))

    def selectCloseDDButton(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//i[@class='fa-light fa-close']")))

    def getListAlldependantProfile(self):
        return self.driver.find_elements(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/label/span')

    def getSecondDependantNameFromProfileDD(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/label/span")))

    def GetSelectedMemberCount(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'member-select')]/i[2]//following::span[1]")))

    def getAllMemberFromHomePageDropdown(self):
        return self.driver.find_elements(By.XPATH,"//div[@class='select-member']/label/span")

    def getAllDependantMemberListHomePageDrodown(self):
        return self.driver.find_elements(By.XPATH,"//*[text()[contains(.,'Dependent')]]")

    def getUpdateButtoninMemberDropdown(self):
        return   WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='button-action']")))

    def getcheckboxesForMemberDropdown(self):
        return  self.driver.find_elements(By.XPATH,"//input[@type='checkbox']")


