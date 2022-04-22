import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Common.Variables.variables import VariablesClass
from Pages.Login.LogInPage import LogInClass
from Pages.Password.PasswordPage import PasswordClass
from Pages.Main.NavigationBar.NavigationBar import NavigationBarClass
from Pages.Main.NavigationBar.PopUpMenu.PopUPMenu import AccountAndListClass
from Pages.Main.SearchResultPage.SearchResultPage import SelectElementClass
from Pages.Main.SearchResultPage.ProductInfoPage import ProductInfoPageClass


class LogInLogoutAddProductSignOutTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variables = VariablesClass()
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)
        cls.loginPage = LogInClass(cls.driver)
        cls.passwordPage = PasswordClass(cls.driver)
        cls.navBar = NavigationBarClass(cls.driver)
        cls.accoutAndList = AccountAndListClass(cls.driver)
        cls.selectElement = SelectElementClass(cls.driver)
        cls.productInfoPageClass = ProductInfoPageClass(cls.driver)

    def setUp(self):
       pass

    def test_PositiveLogInLogoutAddProduct(self):
        self.driver.get(self.variables.url)
        self.loginPage.fill_login_field()
        self.loginPage.press_into_continue_button()
        self.passwordPage.fill_password()
        self.passwordPage.click_Keep_me_signed_in()
        self.passwordPage.click_into_SignIn_button()
        self.navBar.fill_search_field()
        self.selectElement.select_the_first_element_from_search_result()
        self.productInfoPageClass.add_item_to_cart()
        self.productInfoPageClass.click_into_close_button()
        self.navBar.click_account_list()

        time.sleep(5)

    def tearDown(self):
        self.accoutAndList.click_sign_out_button()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()