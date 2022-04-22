from Locators.Locators import LocatorsClass
from Common.CustomFind.FindElement import CustomFindElement
from Common.Variables.variables import VariablesClass


class BaseClass():
    def __init__(self, driver):
        self.driver = driver
        self.locators = LocatorsClass()
        self.customFind = CustomFindElement(self.driver)
        self.variables = VariablesClass()
