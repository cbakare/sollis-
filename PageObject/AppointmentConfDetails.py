from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppointmentDetails():
    def __init__(self, driver):
        self.driver = driver

    def getAllheaders(self):
        return  self.driver.find_elements(By.XPATH,"//div[@class='apt-section row']/div/p[@class='headfont']")

    def getUserDataUnderheader(self):
        return  self.driver.find_elements(By.XPATH,"//div[@class='apt-section row']/div/p//following::span")

    def getPrefferedTime(self):
        return  WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Preferred Time']//following::p")))

    def getConfirmationButton(self):
        return  WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,"//div[text()='create appointment']")))

    def getValueforRequestForHeader(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='apt-section row']/div/p//following::span")))

    def getValueForMemberAttendingAppointment(self):
        return WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div[3]/div/div/div[2]/div/div/div/div/div/div[1]/div")))

    def getValueForHouseCallAddress(self):
        return WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".apt-addr")))

    def getValueForSpecialInstruction(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//textarea[@class='form-control']")))

    def getValueForPhoneNumber(self):
        return WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@class='form-control']")))

    def getValuePreffereTime(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[@class='date link']")))

    def getAppointConfirmationPageLoaded(self):
        return WebDriverWait(self.driver,25).until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(),'Appointment Confirmation')]")))






