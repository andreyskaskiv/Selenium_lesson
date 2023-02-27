import datetime
import os
import time
import unittest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import img
from definitions import PATH_TO_TESTING_SAUCEDEMO_COM_IMG
from tools.utils import run as create_gif_animation

PATH_TO_IMG = os.path.join(Path(img.__file__).parent)


class TestSaucedemoCom(unittest.TestCase):
    now_date = None
    chrome_options = None
    browser: webdriver.chrome = None
    url: str = None

    LOGIN_TEST = "standard_user"
    PASSWORD_TEST = "secret_sauce"

    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome_options = Options()
        # cls.chrome_options.add_argument("--headless")  # without GUI
        # cls.service = Service(executable_path=r"tests_integration/chromedriver.exe")

        cls.browser = webdriver.Chrome(options=cls.chrome_options)
        cls.action = ActionChains(cls.browser)

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
        self.create_screenshot(self._testMethodName)
        """clear"""
        self.browser.find_element(By.XPATH, '//input[@data-test="username"]').clear()
        self.create_screenshot(self._testMethodName)
        self.browser.find_element(By.XPATH, '//input[@data-test="username"]').send_keys(self.LOGIN_TEST)
        self.browser.find_element(By.CSS_SELECTOR, '#password').send_keys(self.PASSWORD_TEST)
        self.create_screenshot(self._testMethodName)

        """ Click to button LOGIN """
        self.browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(1)

        self.create_screenshot(self._testMethodName)
        self.assertEqual(self.browser.title, 'Swag Labs')

    def test_02_keys(self):
        """Drop down menu navigation"""
        self.browser.find_element(By.XPATH, '//select[@data-test="product_sort_container"]').click()
        self.create_screenshot(self._testMethodName)
        self.browser.find_element(By.XPATH, '//select[@data-test="product_sort_container"]').send_keys(Keys.DOWN)
        self.create_screenshot(self._testMethodName)
        self.browser.find_element(By.XPATH, '//select[@data-test="product_sort_container"]').send_keys(Keys.DOWN)
        self.create_screenshot(self._testMethodName)
        self.browser.find_element(By.XPATH, '//select[@data-test="product_sort_container"]').send_keys(Keys.UP)
        self.create_screenshot(self._testMethodName)
        self.browser.find_element(By.XPATH, '//select[@data-test="product_sort_container"]').send_keys(Keys.RETURN)
        time.sleep(1)
        self.create_screenshot(self._testMethodName)

        self.T_shirt_name = self.browser.find_element(By.XPATH, '//a[@id="item_3_title_link"]').text
        self.assertEqual(self.T_shirt_name, 'Test.allTheThings() T-Shirt (Red)')

    def test_03_scroll(self):
        """Scroll to footer"""
        self.footer = self.browser.find_element(By.XPATH, '//*[@id="page_wrapper"]/footer/div')
        self.action.move_to_element(self.footer).perform()

        self.footer_text = self.browser.find_element(By.XPATH, '//*[@id="page_wrapper"]/footer/div').text
        time.sleep(1)
        self.create_screenshot(self._testMethodName)
        self.assertEqual(self.footer_text, '© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy')

    def test_04_hidden_menu(self):
        """Hidden menu"""
        self.browser.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
        time.sleep(1)
        self.create_screenshot(self._testMethodName)
        self.browser.find_element(By.XPATH, '//a[@id="about_sidebar_link"]').click()
        time.sleep(1)
        self.create_screenshot(self._testMethodName)

        """Get current_url"""
        self.about_url = self.browser.current_url
        self.assertEqual(self.about_url, 'https://saucelabs.com/')

    def test_05_working_with_browser_history(self):
        """History browser"""
        self.browser.back()
        self.browser.forward()
        time.sleep(1)
        self.create_screenshot(self._testMethodName)
        self.browser.back()
        time.sleep(1)
        self.create_screenshot(self._testMethodName)

        """Get current_url"""
        self.about_url = self.browser.current_url
        self.assertEqual(self.about_url, 'https://www.saucedemo.com/inventory.html')

        create_gif_animation(PATH_TO_TESTING_SAUCEDEMO_COM_IMG)


if __name__ == '__main__':
    unittest.main()

