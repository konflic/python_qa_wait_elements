from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.my_expected_conditions import my_custom_condidion


def wait_for_element_locates(driver, locator, timeout=3):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        driver.save_screenshot("exception.png")
        raise AssertionError(f"Элемент {locator} не появился на странице за 2 сек.")


def wait_for_elements_amount_presence(driver, locator: tuple, amount=4, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(my_custom_condidion(locator, amount))
    except TimeoutException:
        driver.save_screenshot("exception.png")
        raise AssertionError(f"Не дождался нужного количества ({amount}) элементов {locator} на странице")

def my_find_element(driver, locator: tuple):
    return driver.find_element(*locator)