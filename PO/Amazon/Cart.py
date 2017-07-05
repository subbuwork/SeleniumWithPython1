from selenium import webdriver


class Cart(object):

    def __init__(self,driver):
        self.driver = driver

    def proceed_to_checkout(self):
        self.driver.find_element_by_xpath("//a[@id='hlb-ptc-btn-native']").click()
        self.driver.get_screenshot_as_file(
            "C:\\Users\\subbu\\PycharmProjects\\Excercise1\\Screenshots\\amazon\\signInpage.png")

    def verify_cart(self):
        self.driver.find_element_by_id("hlb-view-cart-announce").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//span[@id='sc-buy-box-ptc-button']/span/input").click()
        self.driver.get_screenshot_as_file(
            "C:\\Users\\subbu\\PycharmProjects\\Excercise1\\Screenshots\\amazon\\cartverificationpage.png")
