from pages.base_page import BasePage
from components.components import WebElement

class FormsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'Forms'}

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender = WebElement(driver, '#gender-radio-3')
        self.phone = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self. btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.user_form = WebElement(driver, '#userForm')
        self.btn_state_menu = WebElement(driver, '#state > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)')
        self.state_line = WebElement(driver, '#react-select-3-input')
        #self.btn_city_menu = WebElement(driver, '.css-1fhf3k1-control > div:nth-child(2) > div:nth-child(2)')
        #self.city_line = WebElement(driver,'.css-1fhf3k1-control > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)')

