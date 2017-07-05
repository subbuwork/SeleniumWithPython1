from selenium import webdriver


def test1():
    driver = webdriver.Chrome()
    driver.get("http://facebook.com")
    driver.find_element_by_name("email").send_keys("test")
    driver.find_element_by_id("pass").send_keys("test123")
    driver.find_element_by_link_text("Forgot account?").click()

    driver.quit()