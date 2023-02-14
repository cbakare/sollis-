from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():
    def __init__(self,driver):
        self.driver=driver

    def ImmedieteCareHeaderHomePage(self):
        return  WebDriverWait(self.driver,25).until(EC.visibility_of_element_located((By.XPATH,"//h1[text()='Immediate Care']")))

    def getHomePageLogo(self):
        return  WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='mx-auto']")))