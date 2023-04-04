import time
import allure

from pages.alerts import Alerts
from selenium.webdriver.common.keys import Keys

@allure.title('Проверка видимости alerts')
def test_alerts(browser):
    alerts_page = Alerts(browser)

    alerts_page.visit()
    assert not alerts_page.alert()
    alerts_page.btn_alert.click()
    time.sleep(2)
    assert alerts_page.alert()
    alerts_page.alert().accept()

@allure.title('Проверка текста alert')
def test_alert_text(browser):
    alert_text = Alerts(browser)

    alert_text.visit()
    alert_text.btn_alert.click()
    time.sleep(2)
    assert alert_text.alert().text == 'You clicked a button'
    time.sleep(2)
    alert_text.alert().accept() #чтоб подтвердить алерт
    assert not alert_text.alert() #убедиться, что алерта уже нет


@allure.title('Проверка confirm')
def test_confirm(browser):
    confirm_page = Alerts(browser)

    confirm_page.visit()
    confirm_page.btn_confirm.click()
    time.sleep(2)
    confirm_page.alert().dismiss()
    time.sleep(2)
    assert confirm_page.btn_canceled.get_text() == 'You selected Cancel'



@allure.title('Проверка вода текста promt')
def test_promt(browser):
    promt_text = Alerts(browser)

    promt_text.visit()
    promt_text.btn_promt.click()
    time.sleep(2)
    promt_text.alert().send_keys('name')
    promt_text.alert().accept()
    assert promt_text.btn_text.get_text() == 'You entered name'

