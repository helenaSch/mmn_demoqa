import time

from pages.droppable import Droppable
from selenium.webdriver import ActionChains
def test_drag_and_drop(browser):
    action_chains = ActionChains(browser)
    page = Droppable(browser)

    page.visit()

    # action_chains.drag_and_drop(
    #     page.grag.find_element(),
    #     page.drop.find_element()
    # ).perform()
    assert page.grag.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(
        page.grag.find_element(),
        page.drop.find_element()
    ).perform()
    time.sleep(2)

    assert page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(1)

    action_chains.drag_and_drop_by_offset(
        page.grag.find_element(),
        -200, 0
    ).perform()
    time.sleep(1)
    assert page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')

