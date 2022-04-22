from Pages.Common.BaseClass import BaseClass


class SelectElementClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.getItemAttribute = "Attribute"

    def select_the_first_element_from_search_result(self):
        selectedItem = self.customFind.find_element(self.locators.selectItem)
        selectedItem.click()

    def get_selected_item_name_attribute(self):
        self.getItemAttribute = self.customFind.find_element(self.locators.selectItem).get_attribute("alt")
        print("Getting attribute before checking :", str(self.getItemAttribute))
        return self.getItemAttribute
