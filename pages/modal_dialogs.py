from pages.base_page import BasePage
from components.components import WebElement
class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'Modal Dialogs'
        }

        self.btns_sidebar = WebElement(driver, '.show > ul > li')
        self.btns_btns = WebElement(driver, 'div.element-group')
        self.icon = WebElement (driver, '#app > header:nth-child(1) > a')