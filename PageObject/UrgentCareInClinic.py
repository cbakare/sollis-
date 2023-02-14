from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrgentCare():
    def __init__(self, driver):
        self.driver = driver

    def getListForAllprimarySymtoms(self):
        return  self.driver.find_elements(By.XPATH,"//div[@class='label false col-lg-6']/a")

    def getFirstSymptopns(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[3]/div[1]/p")))

    def checkSubmitButtonisclickable(self):
        return  WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Next']")))