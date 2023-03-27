from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage

def test_navigation(browser):
    navigation_demoqa = DemoQA(browser)
    navigation_el = ElementsPage(browser)

    navigation_demoqa.visit()
    navigation_demoqa.btn_elements.click()

    navigation_demoqa.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert navigation_el.equal_url()

