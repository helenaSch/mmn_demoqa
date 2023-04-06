import time
import allure
import httplib
import re

from pages.modal_dialogs import ModalDialogs


@allure.title('Проверка кнопок, большой и маленькой')
def test_modals(browser):
    modals_page = ModalDialogs(browser)

    modals_page.visit()
    modals_page.small_modal.click()
    time.sleep(2)
    modals_page.btn_close_s.click()
    modals_page.large_modal.click()
    time.sleep(2)
    modals_page.btn_close_l.click()


    #browser.is_page_available('https://demoqa.com/modal-dialogs')