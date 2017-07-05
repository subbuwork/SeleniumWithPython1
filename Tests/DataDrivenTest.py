from selenium import webdriver
import xlrd
import pytest
import time


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Firefox()
    driver.maximize_window()
    #driver.implicitly_wait(30)
    yield driver
    driver.quit()
    #driver.get("http://facebook.com")


def test_ddt(setup):
    driver = setup
    driver.get("http://facebook.com")
    wb = xlrd.open_workbook("C:\Users\subbu\Desktop\Book.xlsx")
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    for row in range(sheet.nrows):
        try:
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys(sheet.cell_value(row,0))
            driver.find_element_by_id("pass").clear()
            driver.find_element_by_id("pass").send_keys(sheet.cell_value(row,1))
            driver.find_element_by_xpath("//input[@value='Log In']").click()
            time.sleep(2)
        except:
            print "Exception occured..."
            driver.find_element_by_id("loginbutton").click()



