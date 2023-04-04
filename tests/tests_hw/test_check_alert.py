import time
import allure

from pages.alerts import Alerts

@allure.title('Проверка кнопки alert')
def test_alerts(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_timer.click()
    time.sleep(6)
    alert_page.alert().accept()