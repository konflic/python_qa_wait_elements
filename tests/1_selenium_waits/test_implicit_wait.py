from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_header_explicit(browser):
    browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
    WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#header"))
    )
    WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".box"))
    )
