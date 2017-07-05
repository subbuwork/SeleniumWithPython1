from selenium import webdriver


def test_demo1():
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
    print "Current url::", browser.current_url
    print "Title::", browser.title

    browser.get("https://www.facebook.com")
    print "Current url::", browser.current_url
    print "Title::", browser.title

    browser.back()
    print "Current url::", browser.current_url
    print "Title::", browser.title

    browser.forward()
    print "Current url::", browser.current_url
    print "Title::", browser.title

    browser.close()
    browser.quit()
