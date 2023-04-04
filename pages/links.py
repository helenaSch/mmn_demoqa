from pages.base_page import BasePage
from components.components import WebElement
class Links(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/links'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'Links'
        }

        self.home_link = WebElement(driver, '#simpleLink')