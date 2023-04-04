import time
import allure

from pages.webtables import WebTables
@allure.title('Проверка сортировки')
def test_one(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    web_tables.btn_first.click()
    web_tables.btn_last.click()
    web_tables.btn_age.click()
    web_tables.btn_email.click()
    web_tables.btn_salary.click()
    web_tables.btn_department.click()
