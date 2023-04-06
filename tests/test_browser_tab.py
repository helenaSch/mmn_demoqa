import time
import allure

from pages.browser_tab import BrowserTab

@allure.title('Проверка перехода на вкладку')
def test_browser_tab(browser):
    browser_page = BrowserTab(browser)

    browser_page.visit()
    assert len(browser.window_handles) == 1
    browser_page.new_tab.click()
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
    #browser_page.current_url()
    #assert browser_page.equal_url() == 'https://demoqa.com/sample'
    assert len(browser.window_handles) == 2
    #assert browser_page.equal_url()

    time.sleep(2)