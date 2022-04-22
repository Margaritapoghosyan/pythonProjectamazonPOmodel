import time
from Pages.Common.BaseClass import BaseClass


class LogInClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)


    def fill_login_field(self):
        loginField = self.customFind.find_element(self.locators.LoginPageLoginFieldLocator)
        loginField.send_keys(self.variables.login)
        time.sleep(4)

    def press_into_continue_button(self):
        continueButton = self.customFind.find_element(self.locators.LoginPageContinueButtonLocator)
        continueButton.click()
