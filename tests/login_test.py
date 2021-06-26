from selenium import webdriver
import pytest
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils import utils as utils
import allure
import pendulum

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "abc"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = pendulum.now().strftime("%d-%m-%Y::%H:%M:%S")
            testName = utils.whoami()
            screenShotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenShotName,
                          attachment_type=allure.attachment_type.PNG)
            raise

        except:
            print("There is an exception")

            currTime = pendulum.now().strftime("%d-%m-%Y::%H:%M:%S")
            testName = utils.whoami()
            screenShotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenShotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("/home/rahul/PycharmProjects/AutomationFramework/screenshots" + screenShotName + ".png")

            raise

        else:
            print("No exceptions occurred")

        finally:
            print("This block will always execute | Close DB")


