import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login.LogInPage import LogInClass
from Pages.Password.PasswordPage import PasswordClass
from Common.Variables.variables import VariablesClass
from Pages.Main.NavigationBar.NavigationBar import NavigationBarClass
from Pages.Main.NavigationBar.Cart.Cart import ShoppingCartClass
from Pages.Main.NavigationBar.PopUpMenu.PopUPMenu import AccountAndListClass
from Pages.Main.SearchResultPage.SearchResultPage import SelectElementClass
from Pages.Main.SearchResultPage.ProductInfoPage import ProductInfoPageClass
from Pages.Main.NavigationBar.PopUpMenu.Recommendation import RecommendationClass


class AmazonTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variables = VariablesClass()
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)
        cls.loginPage = LogInClass(cls.driver)
        cls.passwordPage = PasswordClass(cls.driver)
        cls.navigationBar = NavigationBarClass(cls.driver)
        cls.selectElement = SelectElementClass(cls.driver)
        cls.productInfoPage = ProductInfoPageClass(cls.driver)
        cls.shoppingCart = ShoppingCartClass(cls.driver)
        cls.accountAndList = AccountAndListClass(cls.driver)
        cls.recommendation = RecommendationClass(cls.driver)


    def setUp(self):
       pass

    def test_PositiveLogInAddProduct(self):

        self.driver.get(self.variables.url)
        self.loginPage.fill_login_field()
        self.loginPage.press_into_continue_button()
        self.passwordPage.fill_password()
        self.passwordPage.click_Keep_me_signed_in()
        self.passwordPage.click_into_SignIn_button()
        self.navigationBar.fill_search_field()
        self.selectElement.get_selected_item_name_attribute()
        self.selectElement.select_the_first_element_from_search_result()
        self.productInfoPage.add_item_to_cart()
        self.productInfoPage.click_into_close_button()
        self.navigationBar.press_into_cart_button()
        self.shoppingCart.check_item_in_cart(self.selectElement.getItemAttribute)
        self.shoppingCart.delete_item_from_cart()
        self.navigationBar.click_account_list()
        self.accountAndList.click_into_Recomendation()
        self.recommendation.select_element_from_recommendation()
        self.recommendation.open_choosen_product()


        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
