from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Appoinments():

    def __init__(self, driver):
        self.driver = driver

    def getAppointmentLinkOnHomePage(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'appointment-label')]")))

    def getListOfAppointments(self):
        return self.driver.find_elements(By.XPATH,"//div[contains(@class,'appointment-label")
