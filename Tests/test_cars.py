from selenium import webdriver
import pytest
import time
import logging
from Utils import Browser
from Resources import CarsApp
from Config import CarsProperties

input_data_for_make_search = {"car_type":"new", "make":"Honda", "model":"All Models", "price":"$45,000", "miles":"40 Miles from", "zip_code":"28262", "locators_for":"make"}
input_data_for_body_style_search = {"car_type":"new", "body_style":"Coupe", "price":"$45,000", "miles":"40 Miles from", "zip_code":"28262","locators_for":"body"}


@pytest.fixture(scope="module")
def setup():
    driver = Browser.Browser().open_browser("ff")
    yield driver
    driver.quit()


def test_cars_home_page(setup):
    CarsApp.cars_home_page(setup, CarsProperties.urls["cars"])


def test_cars_home_page_header_menus(setup):
    CarsApp.cars_home_page(setup, CarsProperties.urls["cars"])
    CarsApp.cars_home_page_header_menu(setup)


def test_cars_home_page_vehicle_search_menu(setup):
    CarsApp.cars_home_page(setup,CarsProperties.urls["cars"])
    CarsApp.cars_home_page_search_menu(setup)


def test_search_cars_by_make(setup):
    CarsApp.cars_home_page(setup, CarsProperties.urls["cars"])
    CarsApp.search_car_by_make(setup,input_data_for_make_search)


def test_search_cars_by_body_style(setup):
    CarsApp.cars_home_page(setup, CarsProperties.urls["cars"])
    CarsApp.search_cars_by_body_style(setup,input_data_for_body_style_search)


