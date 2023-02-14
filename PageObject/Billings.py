# Home page link-//p[text()='Billing']
# unread count- //p[text()='Billing']//following::span
# header for billing - //h4[@class='header-text text-center']
# test type - column header - //table/thead[@data-test='datatable-head']/tr[1]/th[2]/span
# result column header -  //table/thead[@data-test='datatable-head']/tr[1]/th[3]/span
# complete rows of the table =//table/tbody[@data-test='table-body']/tr/td[2]
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Billings():
    def __init__(self,driver):
        self.driver=driver

    def getBillingHomePageLink(self):
        return WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Billing']")))

    def getUnreadBillingCount(self):
        return  WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Billing']//following::span")))

    def getBillingHeaderAtBillingPage(self):
        return  WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,"//h4[@class='header-text text-center']")))

    def getBillingColumnheader_Filename(self):
        return  WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,"//table/thead[@data-test='datatable-head']/tr[1]/th[2]/span")))

    def getBillingColumnheader_Date(self):
        return  WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,"//table/thead[@data-test='datatable-head']/tr[1]/th[3]/span")))

    def getBillingColumnheaders(self):
        return  self.driver.find_elements(By.XPATH,"//table/tbody[@data-test='table-body']/tr/td[2]")