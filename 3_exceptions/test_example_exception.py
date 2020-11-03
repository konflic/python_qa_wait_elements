from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_title(title, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        raise TimeoutException("Ждал что title будет: '{}' но он был '{}'".format(title, driver.title))


def assert_element(selector, driver, timeout=1):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        # Обрабатываем, выбрасываем своё исключение и атачим скриншот
        driver.save_screenshot("{}.png".format(driver.session_id))
        raise AssertionError("Не дождался видимости элемента: {}".format(selector))


def test_check_exception(browser):
    browser.get("https://konflic.github.io/front_example/")
    wait_title("Example Project", browser)
    assert_element("[name='disable']", browser)

