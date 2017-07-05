from selenium import webdriver
from Config import CarsProperties
import time

class CarsAppHomePage(object):
    def __init__(self,driver):
        self.driver = driver

    def open_homepage(self,url):
        self.driver.get(url)
        #self.driver.execute_script("window.scrollTo(0,250);")
        #time.sleep(1)
        #self.driver.execute_script("window.scrollTo(250,500);")

        self.driver.get_screenshot_as_file(CarsProperties.screen_shot_location + "\\" + "carshomepage.png")

