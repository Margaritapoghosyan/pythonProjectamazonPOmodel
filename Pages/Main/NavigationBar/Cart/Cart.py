import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.Common.BaseClass import BaseClass


class ShoppingCartClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def check_item_in_cart(self, attribute):
        self.myAttribute = attribute
        print("Get attribute after checking :", self.myAttribute)
        try:
            if self.myAttribute in self.driver.page_source:
                pass
            print("Selected element in cart")

        except NoSuchElementException:
            print("No such element in cart")
        time.sleep(2)

    def delete_one_item(self):
        deleteItm = self.customFind.find_element(self.locators.delItem)
        deleteItm.click()

    def delete_item_from_cart(self):
        try:
            for delete in self.driver.page_source:
                deleteItm = self.customFind.find_element(self.locators.delItem)
                deleteItm.click()
        except:
            print("The shopping cart is empty")
        time.sleep(2)
