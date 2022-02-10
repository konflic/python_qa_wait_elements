import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def driver_factory(browser):
    if browser == "chrome":
        service = Service(executable_path=os.path.join(DRIVERS, "chromedriver"))
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "opera":
        driver = webdriver.Opera()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture
def browser(request):
    driver = driver_factory(request.config.getoption("--browser"))
    driver.maximize_window()
    # driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver
