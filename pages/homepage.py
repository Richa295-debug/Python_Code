import self
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver


class HomePage(SeleniumDriver):

    welcome_field = "welcomeMessage"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def get_welcome_text(self):
        return self.get_element(self.welcome_field,"class").text
        #return self.get_element(self.welcome_field,"class").text






