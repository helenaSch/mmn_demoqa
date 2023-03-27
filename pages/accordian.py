from pages.base_page import BasePage
from components.components import WebElement
class AccordianPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'Accordian'

        }
        self.accordian_element = WebElement(driver, '#section1Content')
        self.accordian_header = WebElement(driver, '#section1Heading')
        self.accordian_1_element = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.accordian_2_element = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.accordian_3_element = WebElement(driver, '#section3Content > p')
