from selenium import webdriver
import logging
from selenium.webdriver.support.ui import Select
from Config import Locators,CarsProperties


class WebElementLocator(object):
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

# Header menu web element locators
    def cars_header_menu_buy(self):
        logging.getLogger("cars_header_menu_buy")
        self.driver.find_element_by_xpath(Locators.buy).click()
        self.driver.get_screenshot_as_file(CarsProperties.screen_shot_location + "\\" + "buymenu_page.png")

    def cars_header_menu_sell(self):
        self.driver.find_element_by_xpath(Locators.sell).click()
        self.driver.get_screenshot_as_file(CarsProperties.screen_shot_location + "\\" + "sellmenu_page.png")

    def cars_header_menu_services(self):
        self.driver.find_element_by_xpath(Locators.services).click()
        self.driver.get_screenshot_as_file(CarsProperties.screen_shot_location + "\\" + "servicesmenu_page.png")

    def cars_header_menu_news(self):
        self.driver.find_element_by_xpath(Locators.news).click()
        self.driver.get_screenshot_as_file(CarsProperties.screen_shot_location + "\\" + "newsmenu_page.png")

    def cars_header_menu_profile(self):
        self.driver.find_element_by_xpath(Locators.profile).click()
        self.driver.get_screenshot_as_file(CarsProperties.screen_shot_location + "\\" + "profilemenu_page.png")

    # Search menu web element locators

    def cars_search_menu(self):
        self.driver.find_element_by_xpath(Locators.search).click()
        self.driver.get_screenshot_as_file(
            CarsProperties.screen_shot_location + "\\" + "search_menu\\search_page.png")

    def cars_research_specs(self):
        self.driver.find_element_by_xpath(Locators.research_search).click()
        self.driver.get_screenshot_as_file(
            CarsProperties.screen_shot_location + "\\" + "search_menu\\research_search_page.png")

    def cars_dealers_search(self):
        self.driver.find_element_by_xpath(Locators.dealer_search).click()
        self.driver.get_screenshot_as_file(
            CarsProperties.screen_shot_location + "\\" + "search_menu\\dealer_search_page.png")

    # Search Cars  for Sale locators..

    def car_type(self, car_type):
        type_ele = self.driver.find_element_by_xpath(Locators.type)
        Select(type_ele).select_by_value(car_type)

    def car_make(self, make):
        make_ele = self.driver.find_element_by_xpath(Locators.make)
        Select(make_ele).select_by_visible_text(make)

    def car_model(self, model):
        model_ele = self.driver.find_element_by_xpath(Locators.model)
        Select(model_ele).select_by_visible_text(model)

    def car_price(self, price):
        price_ele = self.driver.find_element_by_xpath(Locators.price)
        Select(price_ele).select_by_visible_text(price)

    def car_miles(self,miles):
        miles_ele = self.driver.find_element_by_xpath(Locators.miles)
        Select(miles_ele).select_by_visible_text(miles)

    def car_zip_code(self,zip_code):
        self.driver.find_element_by_xpath(Locators.pin_code).send_keys(zip_code)

    def car_search(self):
        self.driver.find_element_by_xpath(Locators.search_car).click()

    # Search Car By Body Style Locators

    def cars_click_body_style_tab(self):
        self.driver.find_element_by_xpath(Locators.select_car_body_label).click()

    def cars_select_car_type(self, car_type):
        car_type_ele = self.driver.find_element_by_xpath(Locators.car_type)
        Select(car_type_ele).select_by_visible_text(car_type)

    def cars_select_car_body_style(self,body_style):
        car_body_style_ele = self.driver.find_element_by_xpath(Locators.car_body_style)
        Select(car_body_style_ele).select_by_visible_text(body_style)

    def cars_select_car_body_style_price(self, price):
        car_body_style_price_ele = self.driver.find_element_by_xpath(Locators.car_price)
        Select(car_body_style_price_ele).select_by_visible_text(price)

    def cars_select_car_body_style_miles(self, miles):
        car_body_style_miles_ele = self.driver.find_element_by_xpath(Locators.car_miles)
        Select(car_body_style_miles_ele).select_by_visible_text(miles)

    def cars_select_car_body_style_zip_code(self, zip_code):
        car_body_style_zip_ele = self.driver.find_element_by_xpath(Locators.car_zip_code)
        Select(car_body_style_zip_ele).select_by_visible_text(zip_code)

    def cars_select_car_body_style_search(self):
        self.driver.find_element_by_xpath(Locators.sear_button)

