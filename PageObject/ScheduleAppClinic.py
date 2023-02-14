from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScheduleAppClinic():

    def __init__(self, driver):
        self.driver = driver

    ScheduleAppLinkHome = (By.XPATH, "//p[text()='Schedule Appointment']")
    ScheduleAppPageHeader = (By.XPATH, "//h1[text()='Schedule Appointments']")
    InClinicHeader = (By.XPATH,"//div/p[text()='In-Clinic']")
    CovidCareClinic =(By.XPATH,"(//div[@class='schedule-label col-lg-4'])[1]")
    AppontmentConfirmPopup=(By.XPATH,"//div[@class='modal-body']")
    AppConfPopupHeader=(By.XPATH,'//div/h4')
    AppConfPopupYesButton=(By.XPATH,"//a[text()='Yes']")

    def NavigateToScheduleAppointmentPage(self):
        return  WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Schedule Appointment']")))
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//h1[text()='Schedule Appointments']")))

    def headerInClinic(self):
        return  self.driver.find_element(*ScheduleAppClinic.InClinicHeader)

    def getCovidCarelinkclinic(self):
        return  WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='icon-5']/i[1]")))

    def getAppConfirmPopup(self):
        return   self.driver.find_element(*ScheduleAppClinic.AppontmentConfirmPopup)

    def getAppConfPopupHeader(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div/h4")))

    def getAppConfPopupYesButton(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Yes']")))

    def getAppConfPopupNoButton(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='No']")))

    def getCovidTestingRadio(self):
        return   WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='option-txt']//span[text()='Antibody']")))

    def selectedOptionforCovidtest(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Covid Testing']//following::span[1]")))

    def getAllCovidVaccinations(self):
        return  self.driver.find_elements(By.XPATH,"//*[@id='root']/div/div[3]/div/div/div[2]/div[2]/div/form/div/div/label/div[2]/span")

    def getImmidieteCarelink(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='appointment-type margin-top-large container']/div[2]/div/div/div[1]/div/div/div[2]/a/p")))

    def getFirstRadioButtonUnderAvailableSlot(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'mm-dd')]/div[1]/div/div/form/div/div[1]/input")))
