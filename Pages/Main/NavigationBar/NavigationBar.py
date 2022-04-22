import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from Pages.Common.BaseClass import BaseClass


class NavigationBarClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_search_field(self):
        searchField = self.customFind.find_element(self.locators.NavBarsearchFildLocator)
        searchField.clear()
        time.sleep(2)
        searchField.send_keys(self.variables.searchElement)
        searchField.send_keys(Keys.ENTER)

    def press_into_cart_button(self):
            cartBtn = self.customFind.find_element(self.locators.cartButton)
            cartBtn.click()


    def cart_button(self):
        cartBtn = self.customFind.find_element(self.locators.cartButton)
        cartBtn.click()

    def click_account_list(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.customFind.find_element(self.locators.accountAndList))
        actions.perform()
        time.sleep(3)