from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InClinic_Vaccination():
    def __init__(self,driver):
        self.driver=driver

    def getInClinicVaccinationLink(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='tab-pane active']/div/div/div[3]/a/p")))

    def getInClinicVaccinationDescribeYourSymptomsTextbox(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//textarea[@id='exampleText']")))

    def getInClinicVaccinationSubmitRequestButton(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//div[text()='SUBMIT REQUEST']")))

    def getInClinicPreventiveHeaderTextForSchedulingText(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".header-text")))

    def getInClinicPreventiveSchedulingConfirmationMessage(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class='pad-all padding-btm col'] p")))

    def getInclinicPreventiveCrossMarkFromMemberDD(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div/div[2]")))

    def getListOfAllVaccinationUnderSelectVaccination(self):
        return self.driver.find_elements(By.XPATH,"//div[contains(@class,'select-type covid')]/div/p")







