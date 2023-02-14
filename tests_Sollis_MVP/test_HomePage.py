import allure
import pytest
from allure_commons.types import AttachmentType

from PageObject.Multimember import Multimember
from utility.BaseClass import BaseClass
from utility.ScheduleCommonMethods import CommonMethod


@pytest.mark.usefixtures("setup")
class Test_HomePage():

    allure.title("Verify Application is updating the count when dependant is getting add from member list")
    def test_VerifyUpdationofDependantfromMultimemberDropdown(self,setup,LoginpageDataloader):
       try:
            base = BaseClass(self.driver)
            base.signin(setup)
            base.Login(LoginpageDataloader)
            member=Multimember(self.driver)
            Select_Count=int(member.GetSelectedMemberCount().text)
            print(Select_Count)
            member.getDropdownDownArow().click()
            common=CommonMethod(self.driver)
            common.updateTheDependantFromMemberDropdown()
            updated_count=int(member.GetSelectedMemberCount().text)
            print(updated_count)
            assert (updated_count==(Select_Count+1))
       except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Multimember",
                           attachment_type=AttachmentType.PNG)

    allure.title("Verify Application is updating the count when dependant is getting remove from member list")
    def test_RemovingDependantFromHomeMemberDropdown(self):
        try:
            member = Multimember(self.driver)
            Select_Count = int(member.GetSelectedMemberCount().text)
            print(Select_Count)
            member.getDropdownDownArow().click()
            common = CommonMethod(self.driver)
            common.UnselectTheDependant()
            updated_count = int(member.GetSelectedMemberCount().text)
            print(updated_count)
            assert (updated_count == (Select_Count - 1))

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Multimember",attachment_type=AttachmentType.PNG)












