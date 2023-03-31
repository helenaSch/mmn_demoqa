import time

from pages.form_page import FormsPage
from selenium.webdriver.common.keys import Keys

def test_login_form(browser):
    forms_page = FormsPage(browser)

    forms_page.visit()
    assert not forms_page.modal_dialog.exist()
    time.sleep(2)
    forms_page.first_name.send_keys(text='boo')
    time.sleep(2)
    forms_page.last_name.send_keys(text='bootwo')
    time.sleep(2)
    forms_page.user_email.send_keys(text='boo@gmail.com')
    time.sleep(2)
    forms_page.gender.click_force()
    forms_page.phone.send_keys(text='9997775456')
    time.sleep(2)
    forms_page.btn_submit.click_force()
    time.sleep(2)

    assert forms_page.modal_dialog.exist()
    time.sleep(2)
    forms_page.btn_close_modal.click_force()
    time.sleep(2)

def test_State_City(browser):
    city_line = FormsPage(browser)


    city_line.visit()
    time.sleep(3)
    city_line.btn_state_menu.scroll_to_element()
    time.sleep(3)
    city_line.state_line.send_keys(text='Uttar Pradesh')
    city_line.state_line.send_keys(Keys.ENTER)


