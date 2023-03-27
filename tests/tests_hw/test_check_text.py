from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage


def test_go_to_elements(browser):
    demo_page = DemoQA(browser)
    demo_element = ElementsPage(browser)

    demo_page.visit()
    assert demo_page.basement_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    demo_page.btn_elements.click()
    assert demo_element.center_text.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    one_element = ElementsPage(browser)

    one_element.visit()
    assert one_element.center2_text.get_text() == 'Elements'
    assert one_element.elements_icon.exist()
    assert one_element.btn_sidebar_first.exist()
    assert one_element.btn_sidebar_first_textbox.exist()
