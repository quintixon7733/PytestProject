import allure
import pytest
from selenium import webdriver


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome("C:\drivers\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()


@allure.description("Validate OrangeHRM with valid login credentials")
@allure.severity(severity_level="CRITICAL")
def test_validateLogin(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.find_element_by_id("txtUsername").clear()
    enter_username("admin")
    driver.find_element_by_id("txtPassword").clear()
    enter_password("admin123")
    driver.find_element_by_id("btnLogin").click()
    try:
        assert "dashboard" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credentials",
                          attachment_type=allure.attachment_type.PNG)


@allure.description("Validate OrangeHRM with valid login credentials")
@allure.severity(severity_level="NORMAL")
def test_InvalidLogin(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.find_element_by_id("txtUsername").clear()
    enter_username("admin")
    driver.find_element_by_id("txtPassword").clear()
    enter_password("admin1234")
    driver.find_element_by_id("btnLogin").click()
    try:
        assert "dashboard" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credentials",
                          attachment_type=allure.attachment_type.PNG)


@allure.step("Enter username as {0}")
def enter_username(username):
    driver.find_element_by_id("txtUsername").send_keys(username)


@allure.step("Enter password as {0}")
def enter_password(password):
    driver.find_element_by_id("txtPassword").send_keys(password)
