import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        service = Service()
        driver = webdriver.Chrome(service=service)
    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        service = Service(executable_path=os.path.join(drivers, "yandexdriver"))
        options.binary_location = "/usr/bin/yandex-browser"
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Driver not supported")

    request.addfinalizer(driver.quit)

    return driver
