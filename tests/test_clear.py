from pages.test_box import TextBox
import time

def test_clear(browser):
    test_box_page = TextBox(browser)


    test_box_page.visit()
    test_box_page.full_name.send_keys(text='boo')
    time.sleep(2)
    test_box_page.full_name.clear()
    time.sleep(2)
    assert test_box_page.full_name.get_text() == ''
    #assert not test_box_page.full_name.exist() == 'boo'