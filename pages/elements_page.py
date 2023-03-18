from pages.base_page import BasePage
from components.components import WebElement
class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.center_text = WebElement(driver, 'Please select an item from left to start practice.')



    #def equal_url_element(self):
        #if self.get_url() == self.base_url:
           # return True
       # return False

