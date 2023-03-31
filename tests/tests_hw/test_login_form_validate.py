import time
from pages.form_page import FormsPage

def test_login_form_validate(browser):
    text_lines = FormsPage(browser)

    text_lines.visit()
    assert text_lines.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert text_lines.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert text_lines.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert text_lines.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    text_lines.btn_submit.click_force()
    time.sleep(2)
    assert text_lines.user_form.get_dom_attribute('class') == 'was-validated'