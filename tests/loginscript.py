import driver
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.webdriverfactory import WebDriverFactory
from pages.homepage import HomePage
from pages.loginpages import LoginPage

@pytest.mark.usefixtures("setup")
class TestLoginScenario():
    import allure

    @allure.title("Test login")
    @allure.description(
        "This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
    @allure.tag("NewUI", "Essentials", "Authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "John Doe")
    @allure.issue("AUTH-123")
    @allure.testcase("TMS-456")
#added new lines to check new changes

    def test_login(self):

        login=LoginPage(self.driver)
        login.login_to_applications("admin@email.com","admin@123")
        home=HomePage(self.driver)
        welcome_msg=home.get_welcome_text()
        assert "Welcome" in welcome_msg
