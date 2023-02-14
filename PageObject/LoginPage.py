from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():

    def __init__(self,driver):
        self.driver=driver

    LoginLink= (By.XPATH, "//a[text()='LOG IN']")


    def getLoginlink(self):
        return  WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='LOG IN']")))

    def getLoginID(self):
        return  WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"email")))

    def getPassword(self):
        return  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID, "password")))

    def getLoginButton(self):
        return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, "next")))