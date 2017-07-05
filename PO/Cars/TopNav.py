from selenium import webdriver
from Helper.LocatorsHelper import WebElementLocator
import time

locator_helper = None


class HeaderMenus(object):

    def __init__(self, driver):
        self.driver = driver
        global locator_helper
        locator_helper = WebElementLocator(driver)

    def cars_header_menus(self):
        time.sleep(2)
        locator_helper.cars_header_menu_buy()
        time.sleep(2)
        locator_helper.cars_header_menu_sell()
        time.sleep(2)
        locator_helper.cars_header_menu_services()
        time.sleep(2)
        locator_helper.cars_header_menu_news()
        time.sleep(2)
        locator_helper.cars_header_menu_profile()
