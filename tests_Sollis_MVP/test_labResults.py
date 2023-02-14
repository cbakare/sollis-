import pytest

from PageObject.Billings import Billings
from PageObject.LabResults import LabResults
from utility.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Test_LabResults():
    def test_VerifyUnreadCountForLabResults(self, setup, LoginpageDataloader):
        base = BaseClass(self.driver)
        base.signin(setup)
        base.Login(LoginpageDataloader)
        labresult=LabResults(self.driver)
        TestCount=len(labresult.getUnhreadCountelementlink())
        if TestCount==0:
            UnreadCount=0
        else:
            UnreadCount=labresult.getUnreadLabresultsCount().text

    def test_verifyTotalRecordsCountUnderLabResults(self):
        labresult = LabResults(self.driver)
        labresult.getTestResultsHomePageLink().click()
        header=labresult.getTestResultsHeaderAtTestResultPage().text
        assert(header=="Lab Results")
        Tabel_column1=labresult.getTestResultsColumnheader_TestType().text
        assert(Tabel_column1=="TEST TYPE")
        # Table_column2=labresult.getTestResultsColumnheader_Results().text
        # assert(Table_column2=="RESULTS")
        Table_column3=labresult.getTestResultsColumnheader_Date().text
        assert(Table_column3=="DATE")
        bills = Billings(self.driver)
        Table_Record_count = len(bills.getBillingColumnheaders())
        print(Table_Record_count)


