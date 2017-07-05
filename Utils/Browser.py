from Utils import Factory


class Browser(object):

    def open_browser(self, browser_name):
        browser = Factory.BrowserFactory(browser_name).open_browser()
        return browser