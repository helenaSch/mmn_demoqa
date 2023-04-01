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