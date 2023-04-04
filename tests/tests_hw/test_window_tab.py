import time
import allure

from pages.links import Links

@allure.title('Ссылочки-текстики')
def test_links(browser):
    links_page = Links(browser)

    links_page.visit()
    links_page.home_link.exist()
    assert links_page.home_link.get_text() == 'Home'
    assert links_page.home_link.get_dom_attribute('href') == 'https://demoqa.com'
    links_page.home_link.click()
    time.sleep(2)

    browser.switch_to.window(browser.window_handles[0])

