# Home page link-//p[text()='Lab Results']
# unread count- //p[text()='Lab Results']//following::span
# header for labs - //h4[@class='header-text text-center']
# test type - column header - //table/thead[@data-test='datatable-head']/tr[1]/th[2]/span
# result column header -  //table/thead[@data-test='datatable-head']/tr[1]/th[3]/span
# Date column header - //table/thead[@data-test='datatable-head']/tr[1]/th[4]/span
# complete rows of the table =//table/tbody[@data-test='table-body']/tr/td[2]

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LabResults():
    def __init__(self,driver):
        self.driver=driver



    def getTestResultsHomePageLink(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Lab Results']")))

    def getUnhreadCountelementlink(self):
       return  self.driver.find_elements(By.XPATH,"//p[text()='Lab Results']//following::span")

    def getUnreadLabresultsCount(self):
        return WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//p[text()='Lab Results']//following::span")))

    def getTestResultsHeaderAtTestResultPage(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//h4[@class='header-text text-center']")))

    def getTestResultsColumnheader_TestType(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//th[@class='sorting']//span[contains(text(),'Test Type')]")))

    def getTestResultsColumnheader_Date(self):
            return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//th[@class='sorting']//span[contains(text(),'Date')]")))

    def getTestResultsColumnheader(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//table/thead[@data-test='datatable-head']/tr[1]/th[4]/span")))

    def getAllRowinTable(self):
        return self.driver.find_elements(By.XPATH, "//table/tbody[@data-test='table-body']/tr/td[2]")