from selenium import webdriver


class BrowserFactory(object):
    driver = None

    def __init__(self, browser_name):
        global driver
        if browser_name == "gc":
            driver = webdriver.Chrome()
            driver.maximize_window()
        elif browser_name == "ie":
            driver = webdriver.Ie()
            driver.maximize_window()
        elif browser_name == "ff":
            driver = webdriver.Firefox()
            driver.maximize_window()
        elif browser_name == "edge":
            driver = webdriver.Edge()
            driver.maximize_window()
        #return driver

    def open_browser(self):
        return driver
