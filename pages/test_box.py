from pages.base_page import BasePage
from components.components import WebElement
class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'Test box'}

        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.text_space = WebElement(driver, '#output > div > p')
        self.text_space2 = WebElement(driver, 'p.mb-1:nth-child(2)')
