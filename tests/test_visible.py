from pages.elements_page import ElementsPage
import time
def test_visible_btn_sidebar(browser):
    sidebar_element = ElementsPage(browser)

    sidebar_element.visit()
    #sidebar_element.btn_sidebar_first.click()
    time.sleep(3)
    #assert sidebar_element.btn_sidebar_first_textbox.exist()
    assert sidebar_element.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    btn_element = ElementsPage(browser)


    btn_element.visit()
    assert btn_element.btn_sidebar_first_checkbox.visible()

    btn_element.btn_sidebar_first.click()
    time.sleep(2)
    assert not btn_element.btn_sidebar_first_checkbox.visible()