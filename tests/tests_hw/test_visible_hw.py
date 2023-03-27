from pages.accordian import AccordianPage
import time
def test_visible_accordian(browser):
    accordian_page = AccordianPage(browser)

    accordian_page.visit()
    assert accordian_page.accordian_element.visible()
    accordian_page.accordian_header.click()
    time.sleep(2)
    assert not accordian_page.accordian_element.visible()


def test_visible_accordian_default(browser):
    accordian_default = AccordianPage(browser)

    accordian_default.visit()
    assert not accordian_default.accordian_1_element.visible()
    assert not accordian_default.accordian_2_element.visible()
    assert not accordian_default.accordian_3_element.visible()

