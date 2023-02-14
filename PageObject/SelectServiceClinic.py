from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelectServiceClinic():
    def __init__(self, driver):
        self.driver = driver

    def getCovidTestingRadio(self):
        return   WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='option-txt']//span[text()='Antibody']")))

    def selectedOptionforCovidtest(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Covid Testing']//following::span[1]")))

    def getCovidVaccinationHeader(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[3]/div/div/div[2]/div[1]/p")))

    def getAllCovidVaccinations(self):
        return  self.driver.find_elements(By.XPATH,"//*[@id='root']/div/div[3]/div/div/div[2]/div[2]/div/form/div/div/label/div[2]/span")

    def getRadioButton(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='option-txt']/span[text()='Pfizer']")))

    def selectedOptionForCovidVaccine(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Covid Vaccinations']//following::span[1]")))

    def getAllOptionsforpFizer(self):
        return  self.driver.find_elements(By.XPATH,'//div[@class="sub-accord"]/div/label/div[2]/span')

    def getFirstOptionUnderPfizer(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='option-txt']/span[text()='First Dose']")))

    def getSelectedStringVaccination(self):
        return  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[3]/div/div/div[2]/div[1]/span")))

    def  getSubmitButton(self):
        return  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='button-action' and text()='Next']")))

    def primarySelectMemberForTreatmentDD(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".css-12jo7m5")))

    def primarySelectMemberForTreatmentDDforMultiselctValue(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".css-qc6sy-singleValue")))

    def  getBydefaultSelectedValueInDD(self):
        return  WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[5]/div/div/div[1]/div/div/div[1]/div")))

    def getByDefaultSelectedValue1(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'select-state')]/div[1]/div/div[1]/div")))

    def getNY_BydefaultselectedClinic(self):
        return  WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[5]/div/div/div[2]/div/div/div[1]/div")))

    def getOther_BydefaultSelectedClinic(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[5]/div/div/div[2]/div/div/div[1]/div")))

    def getdate_dayforschedilingInclinic(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//button[@class='accordion-button']")))

    def getLatestAvailableDate(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[6]/div/div/div/div[1]/h2/button/text()")))
    def getAllAvailableslots(self):
        return  self.driver.find_elements(By.XPATH,"//*[@id='root']/div/div[6]/div/div/div/div[1]/div/div/form/div/div/label/span")

    def getSubmitButtonAtSelectSelection(self):
        return  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[text()='Next']")))

    def getMemberDDDownArrow(self):
        return  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='row']/div/div/div/div/div[1]/div[2]/div[2]")))

    def getCrossMarkOfDDForSelf(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='row']/div/div/div/div/div[1]/div[2]/div[1]")))

    def getDependantValue(self):
        return  self.driver.find_elements(By.XPATH,"//input[@id='react-select-3-input']")

    def getMemberDropdownArrowfromSelectAppointmentPage(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class ='css-tlfecz-indicatorContainer']//*[name()='svg']")))

    def getAllVaccinationListUnderSelectServicePage(self):
        return self.driver.find_elements(By.XPATH,"//*[@id='root']/div/div[3]/div/div/div[2]/div[2]/div/form/div/div/div/label/div[2]")

    def openCovidVaccinationListAtSelectServicePage(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[normalize-space()='Covid Vaccinations']")))

    def getDosesUnderTheVaccination(self):
        return  self.driver.find_elements(By.XPATH,"//div[@class='sub-accord']/div/label/div[2]/span")

    def ClickOnTheDropdownForMember(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'css-1s2u09g-control')]/div[2]/div[2]")))

    def getCrossMarkForSelectedMember(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='css-xb97g8']")))

    def getDownArrowWhenNoMemberSelectedInMemberDropdown(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'-indicatorContainer')]")))

    def getBydefaultSelectedState(self):
        return WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class ='select-state member-dropdown'] div[class =' css-qc6sy-singleValue']")))
