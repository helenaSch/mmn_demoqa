import time
import allure
from pages.webtables import WebTables
from selenium.webdriver.common.keys import Keys
@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
@allure.severity(allure.severity_level.NORMAL)
def test_one(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    web_tables.btn_add.click()
    time.sleep(2)
    #web_tables.btn_submit.click_force()
    #time.sleep(2)
    #assert web_tables.reg_form.get_dom_attribute('class') == 'was-validated'
    web_tables.full_name.send_keys(text='boo')
    web_tables.last_name.send_keys(text='boo')
    web_tables.email.send_keys(text='boo@gmail.com')
    web_tables.age.send_keys(text='22')
    web_tables.salary.send_keys(text='333')
    web_tables.department.send_keys(text='Magical books')
    web_tables.btn_submit.click_force()
    time.sleep(2)
    assert web_tables.new_line.exist()
    web_tables.pencil.click()
    web_tables.full_name.send_keys(text='qwerty')
    web_tables.btn_submit.click_force()
    assert web_tables.first_cell.get_text() == 'booqwerty'
    web_tables.basket.click()
    assert web_tables.first_cell.get_text() == ' '


@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
@allure.severity(allure.severity_level.NORMAL)
def test_two(browser):
    wt_page = WebTables(browser)

    wt_page.visit()
    wt_page.btn_rows_menu.scroll_to_element()
    time.sleep(3)
    wt_page.btn_rows_menu.send_keys(text='5 rows')
    wt_page.btn_rows_menu.send_keys(Keys.ENTER)
    #assert wt_page.btn_next.isButtonDisabled() == 'disabled'
    #assert wt_page.btn_previous.get_dom_attribute() == 'disabled'
    wt_page.btn_add.click()
    time.sleep(2)
    wt_page.full_name.send_keys(text='boo')
    wt_page.last_name.send_keys(text='boo')
    wt_page.email.send_keys(text='boo@gmail.com')
    wt_page.age.send_keys(text='22')
    wt_page.salary.send_keys(text='333')
    wt_page.department.send_keys(text='Magical books')
    wt_page.btn_submit.click_force()
    time.sleep(2)
    wt_page.btn_add.click()
    time.sleep(2)
    wt_page.full_name.send_keys(text='ludovico')
    wt_page.last_name.send_keys(text='ariosto')
    wt_page.email.send_keys(text='furioso@gmail.com')
    wt_page.age.send_keys(text='58')
    wt_page.salary.send_keys(text='555')
    wt_page.department.send_keys(text='The nonexistent novels')
    wt_page.btn_submit.click_force()
    time.sleep(2)
    wt_page.btn_add.click()
    time.sleep(2)
    wt_page.full_name.send_keys(text='dante')
    wt_page.last_name.send_keys(text='alighieri')
    wt_page.email.send_keys(text='purgatorio@gmail.com')
    wt_page.age.send_keys(text='33')
    wt_page.salary.send_keys(text='666')
    wt_page.department.send_keys(text='Nine black tails')
    wt_page.btn_submit.click_force()
    time.sleep(4)
    #page 1 of 2
    #next button is enable
    wt_page.btn_next.click_force()
    time.sleep(2)
    wt_page.btn_previous.click_force()
    time.sleep(2)


