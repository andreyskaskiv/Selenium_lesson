import datetime
import os
import time
import unittest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import img
from definitions import PATH_TO_DEMOQA_COM_IMG
from tools.utils import run as create_gif_animation

PATH_TO_IMG = os.path.join(Path(img.__file__).parent)


class TestDemoqaCom(unittest.TestCase):
    now_date = None
    chrome_options = None
    browser: webdriver.chrome = None
    url: str = None

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

    def test_01_check_box(self):
        """ check box """
        self.url = "https://demoqa.com/checkbox"
        self.browser.get(self.url)
        self.create_screenshot(self._testMethodName)

        self.browser.find_element(By.XPATH, '//*[@class="rct-icon rct-icon-uncheck"]').click()
        self.create_screenshot(self._testMethodName)

        self.you_have_selected = self.browser.find_element(By.XPATH, '//*[@id="result"]/span[2]').text
        self.assertEqual(self.you_have_selected, 'home')

    def test_02_toggle(self):
        """ check toggle """

        """Home"""
        self.browser.find_element(By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]').click()
        self.create_screenshot(self._testMethodName)
        """Desktop"""
        self.browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()
        self.create_screenshot(self._testMethodName)
        """Notes"""
        self.browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[1]/span/label').click()
        self.create_screenshot(self._testMethodName)
        """Documents"""
        self.browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/button').click()
        self.create_screenshot(self._testMethodName)
        """Office"""
        self.browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/label').click()
        self.create_screenshot(self._testMethodName)

        self.you_have_selected = self.browser.find_element(By.XPATH, '//*[@id="result"]/span[2]').text
        self.assertEqual(self.you_have_selected, 'commands')

    def test_03_radio_button_yes(self):
        """ Radio Button """
        self.url = "https://demoqa.com/radio-button"
        self.browser.get(self.url)
        self.create_screenshot(self._testMethodName)

        self.browser.find_element(By.XPATH, '//label[@for="yesRadio"]').click()
        self.create_screenshot(self._testMethodName)

        self.you_have_selected = self.browser.find_element(By.XPATH, '//span[@class="text-success"]').text
        self.assertEqual(self.you_have_selected, 'Yes')

    def test_04_radio_button_Impressive(self):
        """ Radio Button """
        self.url = "https://demoqa.com/radio-button"
        self.browser.get(self.url)
        self.create_screenshot(self._testMethodName)

        self.browser.find_element(By.XPATH, '//label[@for="impressiveRadio"]').click()
        self.create_screenshot(self._testMethodName)

        self.you_have_selected = self.browser.find_element(By.XPATH, '//span[@class="text-success"]').text
        self.assertEqual(self.you_have_selected, 'Impressive')

    def test_05_button_double_click(self):
        """ Button """
        self.url = "https://demoqa.com/buttons"
        self.browser.get(self.url)
        self.create_screenshot(self._testMethodName)

        self.double_click = self.browser.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
        self.action.double_click(self.double_click).perform()
        self.create_screenshot(self._testMethodName)

        self.you_have_selected = self.browser.find_element(By.XPATH, '//p[@id="doubleClickMessage"]').text
        self.assertEqual(self.you_have_selected, 'You have done a double click')

    def test_06_button_right_click(self):
        """ Button """
        self.right_click = self.browser.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
        self.action.context_click(self.right_click).perform()
        self.create_screenshot(self._testMethodName)

        self.you_have_selected = self.browser.find_element(By.XPATH, '//p[@id="rightClickMessage"]').text
        self.assertEqual(self.you_have_selected, 'You have done a right click')

    def test_07_date_picker(self):
        """ Widgets Date Picker """
        self.url = "https://demoqa.com/date-picker"
        self.browser.get(self.url)
        self.create_screenshot(self._testMethodName)

        self.browser.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]').click()
        self.create_screenshot(self._testMethodName)

        self.browser.find_element(By.XPATH, '//div[@aria-label="Choose Tuesday, February 14th, 2023"]').click()
        self.create_screenshot(self._testMethodName)

        self.browser.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]').click()
        self.create_screenshot(self._testMethodName)

        self.browser.find_element(By.XPATH, '//div[contains(@class, "react-datepicker__day--today")]').click()
        self.create_screenshot(self._testMethodName)

        self.browser.find_element(By.XPATH, '//*[@id="dateAndTimePickerInput"]').click()
        self.create_screenshot(self._testMethodName)

        self.browser.find_element(By.XPATH,
                                  '//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[3]/div[2]/div/ul/li[49]').click()
        self.create_screenshot(self._testMethodName)

    def test_08_slider(self):
        """ Widgets Slider """
        self.url = "https://demoqa.com/slider"
        self.browser.get(self.url)
        self.create_screenshot(self._testMethodName)

        self.slider = self.browser.find_element(By.XPATH, '//*[@id="sliderContainer"]/div[1]/span/input')
        self.action.click_and_hold(self.slider).move_by_offset(20, 0).release().perform()
        self.create_screenshot(self._testMethodName)

        self.slider = self.browser.find_element(By.XPATH, '//*[@id="sliderContainer"]/div[1]/span/input')
        self.action.click_and_hold(self.slider).move_by_offset(-30, 0).release().perform()
        self.create_screenshot(self._testMethodName)

        self.slider_text = self.browser.find_element(By.XPATH, '//*[@id="sliderContainer"]/div[1]/span/div/div[1]').text
        self.assertEqual(self.slider_text, '42')

        create_gif_animation(PATH_TO_DEMOQA_COM_IMG)


if __name__ == '__main__':
    unittest.main()
