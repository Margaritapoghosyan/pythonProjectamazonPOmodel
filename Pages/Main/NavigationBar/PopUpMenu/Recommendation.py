import time
from Pages.Common.BaseClass import BaseClass
from Pages.Main.SearchResultPage.ProductInfoPage import ProductInfoPageClass


class RecommendationClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.productInfo = ProductInfoPageClass(driver)

    def select_element_from_recommendation(self):
        selElement = self.customFind.find_element(self.locators.selectedElement)
        selElement.click()
        self.driver.execute_script("scroll(0,200);")
        time.sleep(5)

    def open_choosen_product(self):
        chosenProduct = self.customFind.find_element(self.locators.openProduct)
        chosenProduct.click()
        try:
            self.productInfo.add_item_to_cart()

        except:
            addToList = self.customFind.find_element(self.locators.addToWishList)
            addToList.click()
