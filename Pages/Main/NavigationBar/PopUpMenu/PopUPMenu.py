import time
from Pages.Common.BaseClass import BaseClass


class AccountAndListClass(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    def click_into_Recomendation(self):
        myrecommendation = self.customFind.find_element(self.locators.recommendation)
        myrecommendation.click()
        time.sleep(2)

    def click_sign_out_button(self):
        mySignOutbutton = self.customFind.find_element(self.locators.signOutButton)
        mySignOutbutton.click()
        time.sleep(2)
