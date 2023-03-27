from pages.base_page import BasePage
from components.components import WebElement
class FormsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'Forms'}

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.gender = WebElement(driver, 'div.custom-radio:nth-child(3) > label')
        self.phone = WebElement(driver, '#userNumber')
