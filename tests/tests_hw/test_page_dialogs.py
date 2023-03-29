import time
from pages.demoqa import DemoQA
from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    modal_page = ModalDialogs(browser)


    modal_page.visit()
    assert modal_page.btns_sidebar.check_count_elements(count=5)
    modal_page.btns_btns.find_elements()

def test_navigation_modal(browser):
    ml_page = ModalDialogs(browser)
    demo_page = DemoQA(browser)

    ml_page.visit()
    ml_page.refresh()
    ml_page.icon.click()
    ml_page.back()
    browser.set_window_size(900, 400)
    time.sleep(2)
    ml_page.forward()
    assert demo_page.equal_url()
    assert browser.title == demo_page.pageData['title']
    browser.set_window_size(1000, 1000)