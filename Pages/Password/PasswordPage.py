import time
from Pages.Common.BaseClass import BaseClass

class PasswordClass(BaseClass):
    def __init__(self, driver):
       super().__init__(driver)

    def fill_password(self):
        passwordField = self.customFind.find_element(self.locators.passwordPagePasswordFieldLocator)
        passwordField.send_keys(self.variables.password)
        time.sleep(4)

    def click_Keep_me_signed_in(self):
        keepMeSigned = self.customFind.find_element(self.locators.KeepMeSigned)
        keepMeSigned.click()
        time.sleep(2)

    def click_into_SignIn_button(self):
        signInButton = self.customFind.find_element(self.locators.passwordPageSignInButtonLocator)
        signInButton.click()
        time.sleep(2)
