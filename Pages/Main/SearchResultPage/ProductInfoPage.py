import time
from Pages.Common.BaseClass import BaseClass



class ProductInfoPageClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def add_item_to_cart(self):
        addToCrtButton = self.customFind.find_element(self.locators.addToCart)
        addToCrtButton.click()
        time.sleep(2)

    def click_into_close_button(self):

        try:
            closeButton = self.customFind.find_element(self.locators.closeButton)
            closeButton.click()
        except:
            print("Close Button not found")
