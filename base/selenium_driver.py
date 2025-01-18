from traceback import print_stack

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumDriver():

    def __init__(self,driver):
        self.driver =driver

    def getbytype(self,locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "name":
            return By.CLASS_NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "class":
            return By.CLASS_NAME

        elif locatorType == "partial_link":
            return By.PARTIAL_LINK_TEXT
        else:
            print("locatorType" +locatorType +"not supported")

    def get_element(self,locator,locatorType="id"):
            element=None
            try:
                bytype=self.getbytype(locatorType)
                element = self.driver.find_element(bytype,locator)
                print("Element found")
            except:
                print("element not found")

            return element

    def click_element(self,locator,locatorType="id"):
            try:
                element = self.get_element(locator,locatorType)
                element.click()
                print("clicked an element")
            except:
                print("cannot clicked")

    def type_element(self,data, locator, locatorType="id"):
            try:
                element = self.get_element(locator, locatorType)
                element.send_keys(data)
                print("Typed data on element")
            except:
                print("Typed data on element")
                print_stack()
    def wait_for_element(self,locator,locatorType="id",timeout=30,pollfrequency=1):
        element=None

        try:
            bytype = self.getbytype(locatorType)
            wait=WebDriverWait(self.driver,timeout,poll_frequency=1)
            element=wait.until(expected_conditions.element_to_be_clickable())
            print("Element found with Ec conditions")
        except:
            print("Element not found with in timeinterval")
        return element