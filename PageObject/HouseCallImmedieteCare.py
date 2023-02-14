from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrgentCare_HouseCall():
    def __init__(self, driver):
        self.driver = driver

    def getHouseCallImmediateCarelink(self):
        return   WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='tab-pane active']//p[@class='headfont'][normalize-space()='Immediate Care']")))

    def getPrimeMemberAtSelectMemberDropdownatHouseCall(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'css-qc6sy-singleValue')]")))

    def getMemberDDDownArrowforHouseCallMemberDD(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//div[@class =' css-tlfecz-indicatorContainer'] // *[name()='svg']")))