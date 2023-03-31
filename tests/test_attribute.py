import allure

from pages.test_box import TextBox
@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
#@allure.severity(allure.severity_level.NORMAL)
@allure.severity(allure.severity_level.BLOCKER)
def test_placeholder(browser):
    """проверка значения атрибута элемента
    severity - важность тест-кейса; blocker, critical, normal, minor"""
    text_attribute = TextBox(browser)

    text_attribute.visit()
    assert text_attribute.full_name.get_dom_attribute('placeholder') == 'Full Name'


def test_fail():
    assert 111 == 222