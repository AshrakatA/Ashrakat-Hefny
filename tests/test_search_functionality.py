import pytest
from selenium.webdriver import Chrome

from pages.GoogleSearchPage import GoogleSearchPage
from pages.GoogleResultsPage import GoogleResultPage

@pytest.fixture
def browser():
    chromeDriver = Chrome()
    chromeDriver.implicitly_wait(10)
    yield chromeDriver
    chromeDriver.quit()

def test_search(browser):
    searchPage = GoogleSearchPage(browser)
    resultPage = GoogleResultPage(browser)
    keyword = 'test'

    #Display google homepage
    searchPage.load()
    searchPage.search(keyword)

    #verify that the result tab title contains the word "test"
    assert keyword in resultPage.title()

    #verify that the search box contain the keyword in result page
    assert keyword == resultPage.SearchInputValue()

    #verify that results contain at least one result having "test' in their title
    assert resultPage.ResultCountForKeyword(keyword)>0