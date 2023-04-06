import time

from pages.slider import Slider
from selenium.webdriver import ActionChains
def test_slider_bar(browser):
    action_chains = ActionChains(browser)
    page = Slider(browser)

    page.visit()
    time.sleep(2)
    assert page.ugle_thing.get_dom_attribute('value') == '25'
    action_chains.drag_and_drop_by_offset(page.ugle_thing.find_element(), 1, 0).perform()
    assert page.ugle_thing.get_dom_attribute('value') == '50'





