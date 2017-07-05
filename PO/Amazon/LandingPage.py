from selenium import webdriver


class LandingPage(object):

    def __init__(self,setup):
        self.setup = setup

    def open_home_page(self, url):
        self.setup.get(url)
        self.setup.get_screenshot_as_file("C:\\Users\\subbu\\PycharmProjects\\Excercise1\\Screenshots\\amazon\\homepage.png")