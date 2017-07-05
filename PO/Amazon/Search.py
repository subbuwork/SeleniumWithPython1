from selenium import webdriver


class SearchPage(object):

    def __init__(self,setup):
        self.setup = setup

    def search_product(self,search_term):
        self.setup.find_element_by_id("twotabsearchtextbox").send_keys(search_term)
        self.setup.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
        self.setup.get_screenshot_as_file("C:\\Users\\subbu\\PycharmProjects\\Excercise1\\Screenshots\\amazon\\searchresultpage.png")