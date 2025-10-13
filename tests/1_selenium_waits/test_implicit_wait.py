from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_header_implicit(browser):
    browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
    browser.find_element(By.CSS_SELECTOR, "#header")
    browser.find_element(By.CSS_SELECTOR, ".box")


def test_check_header_explicit(browser):
    browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
    element = WebDriverWait(driver=browser, timeout=1, poll_frequency=0.1).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#header")),
    )
    
    WebDriverWait(driver=browser, timeout=3).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, ".box")),
    )
