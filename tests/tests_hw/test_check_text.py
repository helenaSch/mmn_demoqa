from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage


def test_go_to_elements(browser):
    demo_page = DemoQA(browser)
    demo_element = ElementsPage(browser)

    demo_page.visit()
    demo_page.basement_text.get_text()

    demo_page.visit()
    demo_element.visit()
    demo_element.center_text.get_text()
