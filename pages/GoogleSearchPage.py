from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleSearchPage:

    URL = 'https://www.google.com'

    searchBox = (By.NAME,'q')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search (self, keyword):
        searchBox = self.browser.find_element(*self.searchBox)
        searchBox.send_keys(keyword + Keys.RETURN)
