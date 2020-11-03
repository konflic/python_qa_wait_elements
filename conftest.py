import pytest
from selenium import webdriver


def driver_factory(browser, driver_folder):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{driver_folder}/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{driver_folder}/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{driver_folder}/operadriver")
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--drivers", default="/usr/local/games")


@pytest.fixture
def browser(request):
    driver = driver_factory(request.config.getoption("--browser"), request.config.getoption("--drivers"))
    driver.maximize_window()
    # driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    return driver
