from pages.elements_page import ElementsPage

def test_find_elements(browser):
    find_element = ElementsPage(browser)

    find_element.visit()
    assert find_element.btns_first_menu.check_count_elements(count=9)
