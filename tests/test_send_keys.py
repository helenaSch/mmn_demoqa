import time

from pages.form_page import FormsPage

def test_send_keys(browser):
    forms_page = FormsPage(browser)

    forms_page.visit()
    forms_page.first_name.send_keys(text='boo')
    time.sleep(3)
    forms_page.last_name.send_keys(text='boo')
    time.sleep(3)

    forms_page.phone.send_keys(text='9999999999')
    time.sleep(3)
