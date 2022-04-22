import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Common.Variables.variables import VariablesClass
from Pages.Login.LogInPage import LogInClass
from Pages.Password.PasswordPage import PasswordClass
from Pages.Main.NavigationBar.NavigationBar import NavigationBarClass
from Pages.Main.NavigationBar.PopUpMenu.PopUPMenu import AccountAndListClass
from Pages.Main.NavigationBar.Cart.Cart import ShoppingCartClass

class delete_all_product_from_cart(unittest.TestCase):
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
        cls.shoppingCart = ShoppingCartClass(cls.driver)
        cls.accoutAndList = AccountAndListClass(cls.driver)


    def setUp(self):
        pass

    def test_PositiveDeletingAllProduct(self):
        self.driver.get(self.variables.url)
        self.loginPage.fill_login_field()
        self.loginPage.press_into_continue_button()
        self.passwordPage.fill_password()
        self.passwordPage.click_Keep_me_signed_in()
        self.passwordPage.click_into_SignIn_button()
        time.sleep(2)
        self.navBar.cart_button()
        self.shoppingCart.delete_item_from_cart()
        self.navBar.click_account_list()

    def tearDown(self):
        self.accoutAndList.click_sign_out_button()
        self.driver.close()