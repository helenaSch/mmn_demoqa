from pages.test_box import TextBox
def test_text_box_submit(browser):
    text_page = TextBox(browser)

    text_page.visit()
    assert text_page.btn_submit.check_css('color', '#fff')
    assert text_page.btn_submit.check_css('backgroundColor', '#007bff')
    assert text_page.btn_submit.check_css('borderColor', '#007bff')
