import unittest
from TestCases.AmazonTestCace.AmazonTestCase import AmazonTestCase
from TestCases.DeleteAllProductFromCart.DeleteAllProductFromCart import delete_all_product_from_cart
from TestCases.LoginLogoutTestCase.LoginLogoutTestCase import LogInLogout
from TestCases.LoginLogoutTestCase.LoginAddProductSignOutTestCase import LogInLogoutAddProductSignOutTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTest(AmazonTestCase("test_PositiveLogInAddProduct"))
    suite.addTest(delete_all_product_from_cart("test_PositiveDeletingAllProduct"))
    suite.addTest(LogInLogout("test_PositiveLogInLogout"))
    suite.addTest(LogInLogoutAddProductSignOutTestCase("test_PositiveLogInLogoutAddProduct"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())