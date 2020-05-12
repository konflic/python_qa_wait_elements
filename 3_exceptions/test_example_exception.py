from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_title(title, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        raise TimeoutException("Ждал что title будет: '{}' но он был '{}'".format(title, driver.title))


def wait_element(selector, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        raise TimeoutException("Не дождался видимости элемента: {}".format(selector))


def test_check_exception(browser):
    browser.get("http://0.0.0.0:8000")
    wait_title("Example", browser)
    wait_element("[name='disabled']", browser)
    # А удобно ли передавать постоянно браузер?
