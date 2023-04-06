import time

from pages.droppable import Droppable
from selenium.webdriver import ActionChains
def test_drag_and_drop(browser):
    action_chains = ActionChains(browser)
    page = Droppable(browser)

    page.visit()

    action_chains.drag_and_drop(
        page.grag.find_element(),
        page.drop.find_element()
    ).perform()
    assert page.grag.check_css('backgroundColor', 'steelblue')
    action_chains.drag_and_drop(

        page.drop.find_element(),
        page.grag.find_element()
    ).perform()
    #action_chains.drag_and_drop_by_offset(page.grag, 800, 300).perform()
    #assert page.drop.check_css('backgroundColor', 'steelblue')
    time.sleep(1)
