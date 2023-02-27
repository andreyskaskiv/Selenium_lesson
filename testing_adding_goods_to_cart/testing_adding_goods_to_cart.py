import datetime
import os
import time
import unittest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import img
from definitions import PATH_TO_TESTING_ADDING_GOODS_TO_CART_IMG
from tools.utils import run as create_gif_animation

PATH_TO_IMG = os.path.join(Path(img.__file__).parent)


class TestGoodsInCart(unittest.TestCase):
    now_date = None
    chrome_options = None
    browser: webdriver.chrome = None
    url: str = None
    product_1 = None
    First_Name = 'Jon'
    Last_Name = 'Conor'
    Zip_Postal_Code = '55555'
    LOGIN_TEST = "standard_user"
    PASSWORD_TEST = "secret_sauce"
    characteristics_goods = []

    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome_options = Options()
        # cls.chrome_options.add_argument("--headless")  # without GUI
        # cls.service = Service(executable_path=r"tests_integration/chromedriver.exe")

        cls.browser = webdriver.Chrome(options=cls.chrome_options)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
        cls.browser.quit()

    @classmethod
    def create_screenshot(cls, filename) -> None:
        """Create screenshot 'test_01_login_2023.02.25_11.55.17.450565.png' """
        cls.now_date = datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S.%f")
        cls.browser.save_screenshot(f"{PATH_TO_IMG}\\{filename}_{cls.now_date}.png")

    def test_01_login(self):
        """ Authorization """
        self.url = "https://www.saucedemo.com/"
        self.browser.get(self.url)
        self.create_screenshot(self._testMethodName)

        """ Fill in the login and password form """
        self.browser.find_element(By.XPATH, '//input[@data-test="username"]').send_keys(self.LOGIN_TEST)
        self.browser.find_element(By.CSS_SELECTOR, '#password').send_keys(self.PASSWORD_TEST)
        self.create_screenshot(self._testMethodName)

        """ Click to button LOGIN """
        self.browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(2)

        self.create_screenshot(self._testMethodName)
        self.assertEqual(self.browser.title, 'Swag Labs')

    def test_02_adding_to_cart(self):
        """ We remember the characteristics of the product """
        self.product_1 = self.browser.find_element(By.XPATH, '//a[@id="item_4_title_link"]').text
        self.price_product_1 = self.browser.find_element(By.XPATH,
                                                         '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text
        """ Click to button ADD TO CART """
        self.browser.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
        self.create_screenshot(self._testMethodName)

        """ Click to CART """
        self.browser.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]').click()
        self.create_screenshot(self._testMethodName)

        """ Goods added to cart"""
        self.product_1_added_to_cart = self.browser.find_element(By.XPATH, '//a[@id="item_4_title_link"]').text
        self.price_product_1_added_to_cart = self.browser.find_element(By.XPATH,
                                                                       '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text

        self.assertEqual(self.product_1, self.product_1_added_to_cart)
        self.assertEqual(self.price_product_1, self.price_product_1_added_to_cart)

        self.characteristics_goods.append((self.product_1, self.price_product_1))

    def test_03_your_information(self):
        """ Fill in the First_Name, Last_Name, Zip_Postal_Code form """

        """Click to button CHECKOUT"""
        self.browser.find_element(By.XPATH, '//button[@id="checkout"]').click()
        """ Fill in the First_Name, Last_Name, Zip_Postal_Code form """
        self.browser.find_element(By.XPATH, '//input[@id="first-name"]').send_keys(self.First_Name)
        self.browser.find_element(By.XPATH, '//input[@id="last-name"]').send_keys(self.Last_Name)
        self.browser.find_element(By.XPATH, '//input[@id="postal-code"]').send_keys(self.Zip_Postal_Code)
        self.create_screenshot(self._testMethodName)

        """Click to button CONTINUE"""
        self.browser.find_element(By.XPATH, '//input[@id="continue"]').click()

        self.checkout_overview = self.browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text
        self.assertEqual(self.checkout_overview, 'CHECKOUT: OVERVIEW')

    def test_04_check_goods(self):
        """Title check"""

        """ We remember the characteristics of the product """
        self.product_1_finished = self.browser.find_element(By.XPATH, '//a[@id="item_4_title_link"]').text

        product_1 = self.characteristics_goods[0][0]
        self.assertEqual(product_1, self.product_1_finished)

    def test_05_check_price(self):
        """Price check"""

        """ We remember the characteristics of the product """
        self.price_product_1_finished = self.browser.find_element(By.XPATH,
                                                                  '//div[@class="inventory_item_price"]').text
        price_product_1 = self.characteristics_goods[0][1]
        self.assertEqual(price_product_1, self.price_product_1_finished)

    def test_06_item_total(self):
        """Total check"""

        self.item_total = self.browser.find_element(By.XPATH,
                                                    '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text
        price_product_1 = self.characteristics_goods[0][1]
        self.create_screenshot(self._testMethodName)
        self.assertEqual(price_product_1, self.item_total)

    def test_07_checkout_complete(self):
        """Checkout complete"""

        """Click to button FINISH"""
        self.browser.find_element(By.XPATH, '//button[@id="finish"]').click()

        self.checkout_complete = self.browser.find_element(By.XPATH, '//h2[@class="complete-header"]').text
        self.create_screenshot(self._testMethodName)
        self.assertEqual(self.checkout_complete, 'THANK YOU FOR YOUR ORDER')

        create_gif_animation(PATH_TO_TESTING_ADDING_GOODS_TO_CART_IMG)


if __name__ == '__main__':
    unittest.main()
