from selenium.webdriver.common.by import By


class GoogleResultPage:

    searchBox = (By.NAME,'q')


    @classmethod
    def KeywordResults(cls, keyword):
        xpath = f"//div[@id='rcnt']//*[contains(text(), '{keyword}')]"
        return (By.XPATH, xpath)

    def __init__(self,browser):
        self.browser = browser


    def ResultCountForKeyword(self,keyword):
        results = self.browser.find_elements(*self.KeywordResults(keyword))
        return len(results)

    def SearchInputValue(self):
        searchInput = self.browser.find_element(*self.searchBox)
        return searchInput.get_attribute('value')

    def title(self):
        return self.browser.title