from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Config import Locators, CarsProperties
from Helper.LocatorsHelper import WebElementLocator

locate = None


class VehicleSearch(object):
    def __init__(self, driver):
        self.driver = driver
        global locate
        locator_helper = WebElementLocator(driver)

    def cars_search_page_menu(self):
        locate.cars_search_menu()
        time.sleep(2)
        locate.cars_research_specs()
        time.sleep(2)
        locate.cars_dealers_search()

    def search_cars(self, input_data):
        if input_data["locators_for"] == "make":
            vSearch = VehicleSearch(self.driver)
            time.sleep(3)
            locate.cars_search_menu()
            time.sleep(3)
            vSearch.search_by_make(input_data)
        elif input_data["locators_for"] == "body":
            vSearch = VehicleSearch(self.driver)
            time.sleep(3)
            locate.vehicle_search_menu()
            time.sleep(3)
            vSearch.search_by_body_style(input_data)

    def search_by_make(self, input_data):
        locate.car_type(input_data["car_type"])
        locate.car_make(input_data["make"])
        locate.car_model(input_data["model"])
        locate.car_price(input_data["price"])
        locate.car_miles(input_data["miles"])
        locate.car_zip_code(input_data["zip_code"])
        locate.car_search()
        self.driver.get_screenshot_as_file(CarsProperties.screen_shot_location + "\\" +
                                           "Search_results\\cars_search_result_page.png")


    def search_by_body_style(self,input_data):
        locate.cars_type(input_data["car_type"])



