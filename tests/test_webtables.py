import time
import allure
import pytest

from pages.webtables import WebTables
@allure.feature('check attr')
@allure.title('Проверка блока No rows found')
def test_page(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    assert web_tables.first_line.exist()
    assert not web_tables.empty_rows.exist()
    while web_tables.del_rows.exist():
        web_tables.del_rows.click()
    time.sleep(2)
    assert web_tables.empty_rows.exist()