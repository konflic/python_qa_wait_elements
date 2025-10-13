from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_title(browser):
    browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
    WebDriverWait(browser, 6).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, ".box")),
        message="Не появился класс с контентом (.box)"
    )
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header")))
