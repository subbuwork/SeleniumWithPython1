from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Product(object):
    def __init__(self,driver):
        self.driver = driver

    def view_product_images(self):
        image_ids = []
        try:
            ele1 = self.driver.find_element_by_xpath("//div[@id='altImages']/ul/li[2]/span/span")
            image_ids.append(ele1)
            ele2 = self.driver.find_element_by_xpath("//div[@id='altImages']/ul/li[3]/span/span")
            image_ids.append(ele2)
            ele3 = self.driver.find_element_by_xpath("//div[@id='altImages']/ul/li[4]/span/span")
            image_ids.append(ele3)
            ele4 = self.driver.find_element_by_xpath("//div[@id='altImages']/ul/li[5]/span/span")
            image_ids.append(ele4)
            for imgid in image_ids:
                ActionChains(self.driver).move_to_element(imgid).perform()
        except:
            for imgid in image_ids:
                hover = ActionChains(self.driver).move_to_element(imgid)
                hover.perform()

        self.driver.implicitly_wait(5)

        hoverele = self.driver.find_element_by_xpath("//*[@id='main-image-container']/ul/li[7]/span/span/div/img")

        ActionChains(self.driver).move_to_element(hoverele).perform()

        self.driver.find_element_by_xpath("//*[@id='main-image-container']/ul/li[7]/span/span/div/img").click()

        self.driver.get_screenshot_as_file("C:\\Users\\subbu\\PycharmProjects\\Excercise1\\"
                                           "Screenshots\\amazon\\productverificationpage.png")
        image_ids1 = []
        try:
            ele5 = self.driver.find_element_by_xpath("//*[@id='ivImage_0']/div")
            image_ids1.append(ele5)
            ele6 = self.driver.find_element_by_xpath("//*[@id='ivImage_1']/div")
            image_ids1.append(ele6)
            ele7 = self.driver.find_element_by_xpath("//*[@id='ivImage_2']/div")
            image_ids1.append(ele7)
            ele8 = self.driver.find_element_by_xpath("//*[@id='ivImage_3']/div")
            image_ids1.append(ele8)
            for id in image_ids1:
                id.click()
        except:
            for id in image_ids1:
                id.click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector(".a-button-close.a-declarative.a-button-top-right").click()

    def check_product_rating_reviews_qa(self):
        ele1 = self.driver.find_element_by_xpath("//span[@id='acrPopover']/span[1]/a/i[1]")
        ActionChains(self.driver).move_to_element(ele1).perform()
        self.driver.get_screenshot_as_file(
            "C:\\Users\\subbu\\PycharmProjects\\Excercise1\\Screenshots\\amazon\\productratingspage.png")

        self.driver.find_element_by_partial_link_text("customer reviews").click()
        self.driver.get_screenshot_as_file(
            "C:\\Users\\subbu\\PycharmProjects\\Excercise1\\Screenshots\\amazon\\productreviewspage.png")
        #self.driver.implicitly_wait(2)

        #self.driver.implicitly_wait(2)
        #self.driver.find_element_by_xpath("//a[@id='askATFLink']").click()
        #self.driver.implicitly_wait(2)

    def select_product_quantity(self,quantity):
        select = Select(self.driver.find_element_by_id("quantity"))
        select.select_by_value(quantity)

    def add_product_to_cart(self):
        self.driver.find_element_by_id("add-to-cart-button").click()
        self.driver.get_screenshot_as_file(
            "C:\\Users\\subbu\\PycharmProjects\\Excercise1\\Screenshots\\amazon\\cartpage.png")
