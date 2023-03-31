from pages.test_box import TextBox
def test_text_box(browser):
    text_page = TextBox(browser)

    text_page.visit()
    text_page.full_name.send_keys(text='boo')
    text_page.current_address.send_keys(text='mir fehlt die zeit')
    text_page.btn_submit.click_force()
    assert text_page.text_space.get_text() == 'Name:boo'
    assert text_page.text_space2.get_text() == 'Current Address :mir fehlt die zeit'





