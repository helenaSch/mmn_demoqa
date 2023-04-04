from pages.base_page import BasePage
from components.components import WebElement
class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'Web Tables'
        }

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.reg_form = WebElement(driver, '#userForm')
        self.full_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.new_line = WebElement(driver, 'div.rt-tr-group:nth-child(4) div')
        self.pencil = WebElement(driver, '#edit-record-4')
        self.first_cell = WebElement(driver, 'div.rt-tr-group:nth-child(4) > div:nth-child(1) > div:nth-child(1)')
        self.basket = WebElement(driver, '#delete-record-4')
        self.btn_rows_menu = WebElement(driver, '.select-wrap select')
        self.btn_next = WebElement(driver, '.-next > button:nth-child(1)')
        self.btn_previous = WebElement(driver, '.-previous > button:nth-child(1)')
        self.pages = WebElement(driver, 'span.-pageInfo >span')

        self.first_line = WebElement(driver, 'div.rt-tr-group:nth-child(1) > div:nth-child(1)')
        self.empty_rows = WebElement(driver, 'div.rt-noData')
        self.del_rows = WebElement(driver, '[title="Delete"]')

        self.btn_first = WebElement(driver, 'div.rt-th:nth-child(1) > div:nth-child(1)')
        self.btn_last = WebElement(driver, 'div.rt-th:nth-child(2) > div:nth-child(1)')
        self.btn_age = WebElement(driver, 'div.rt-th:nth-child(3) > div:nth-child(1)')
        self.btn_email = WebElement(driver, 'div.rt-th:nth-child(4) > div:nth-child(1)')
        self.btn_salary = WebElement(driver, 'div.rt-th:nth-child(5) > div:nth-child(1)')
        self.btn_department = WebElement(driver, 'div.rt-th:nth-child(6) > div:nth-child(1)')