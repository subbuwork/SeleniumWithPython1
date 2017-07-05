from selenium import webdriver


class SelectProduct(object):

    def __init__(self, setup):
        self.setup = setup

    def select_product(self):
        xpath = "//ul[@id='s-results-list-atf']/li[2]/div/div[2]/div/div/a"
        self.setup.find_element_by_xpath(xpath).click()
        self.setup.get_screenshot_as_file("C:\\Users\\subbu\\PycharmProjects\\Excercise1\\Screenshots\\amazon\\productpage.png")