from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_title(browser):
    browser.get("https://konflic.github.io/front_example/pages/slowlyloading.html")
    # Полная сигнатура метода WebdriverWait
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_is("Loaded!"))
    wait.until(EC.visibility_of_element_located((By.ID, "header")), message='')
    el = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), "This is else page content."))
    assert el.text == "This is else page content."


def test_check_magic_button(browser):
    browser.get("https://konflic.github.io/front_example")
    button = browser.find_element_by_name("showjsbutton")
    button.click()
    js_button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "target")))
    js_button.click()
    WebDriverWait(browser, 2).until(EC.staleness_of(button))
    js_button.click()
    WebDriverWait(browser, 2).until(EC.staleness_of(js_button))
