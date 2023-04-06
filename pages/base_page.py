#from selenium.webdriver.common.by import By
from components.components import WebElement
import logging
class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

        self.head_meta = WebElement(driver, 'head > meta')
    def visit(self):
        return self.driver.get(self.base_url)

    #def find_element(self, locator):
        #time.sleep(3)
        #return self.driver.find_element(By.CSS_SELECTOR, locator)

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()



    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False
