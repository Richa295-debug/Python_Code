from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    email_field_value= "email1"
    password_field_value= "password1"
    submit_btn_value="submit-btn"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def login_to_applications(self,email,password):

        self.type_element(email,self.email_field_value,"id")
       # self.driver.find_element(By.ID, "email1").send_keys(email)
        self.type_element(password,self.password_field_value,"id")

        #self.driver.find_element(By.ID, "password1").send_keys(password)
        self.click_element(self.submit_btn_value,"class")
        #self.driver.find_element(By.CLASS_NAME, "submit-btn").click()
