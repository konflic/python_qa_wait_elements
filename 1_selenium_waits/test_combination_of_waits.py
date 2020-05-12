from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_header(browser):
    browser.get("http://0.0.0.0:8000/else.html")
    browser.implicitly_wait(1)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "header")))
