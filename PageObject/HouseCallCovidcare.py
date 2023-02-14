from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HouseCallCovidCare():

    def __init__(self, driver):
        self.driver = driver

    def getHouseCallHeaderLink(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//li[@class='nav-item']/a[1]/p[text()='House Call']")))

    def getHeaderHouseCall(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='tab-pane active']/p[text()='House Call']")))

    def getAllOptionsAvailableUnderHouseCall(self):
        return  self.driver.find_elements(By.XPATH,"//div[@class='card-header']/p")

    def getHouseCallGetCovidCareOption(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[2]/div/div/div[2]/div/div/div[1]/a/p")))

    def getListAllServicesAvailable(self):
        return  self.driver.find_elements(By.XPATH,"//*[@id='root']/div/div[3]/div/div/div/div[1]/p")

    def getRequestAddressforHoueCallHeader(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR," .header-text")))

    def getPrimeMemberAddressForHouseCall(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//form[@class='select-address']/div/div/label/input")))

    def getOtherAlternetAddressForHouseCallRB(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//form[@class='select-address']/div[2]/div/div/label/input")))

    # def getAlternetAddressField(self):
    #     return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='card-body']/div/div[1]/input")))

    def getAlternetAddressField(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='address'][type='text']")))

    # def getAlternetAddressAppartment(self):
    #     return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='card-body']/div/div[2]/input")))

    def getAlternetAddressAppartment(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[name='apartment']")))

    # def getAlternetAddressCity(self):
    #     return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='card-body']/div/div[3]/input")))

    def getAlternetAddressCity(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[name='city']")))

    def getAlternetAddressState(self):
       return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".css-ackcql")))

    def enterAleternetAddressState(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class=' css-ackcql']/input")))

    def getAlternetAddressZipCode(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='zipcode']")))

    def getAlternetAdressSpecialInstruction(self):
        return  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//textarea[@class='form-control']")))

    def getPhoneNuber(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@name='phoneNumber']")))

    def getPrefferedPhoneNumberHeader(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@class='headfont' and text()='Prefered Phone Number']")))

    def  getPrefferedPhoneLabel(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Preferred Phone Number']//following::label[1]")))

    def getASAPradioButton(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@value='ASAP']")))

    def getSubmitRequestButton(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='submit request']")))

    def getHouseCallViewAppointment(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"//a[text()='VIEW APPOINTMENTS']")))

    def getSubmitRequestButtonForHomeappointment(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='section view-apt row']//div[@class='col']")))

    def openCovidTreatmentTabUnderSelectService(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Covid Treatment']")))

    def getAllRadioButtonUnderCovidtreatment(self):
        return self.driver.find_elements(By.XPATH,"//div/label[contains(text(),'type of treatment')]//following::div/input")

    def getViewAppointmentsLink(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//div[text()='VIEW APPOINTMENTS']")))

    def getHouseCallSubmitRequestConfirmationHeader(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//h4[text()='House Call Request']")))


