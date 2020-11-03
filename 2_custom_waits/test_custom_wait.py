from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class amount_of_elements_with_name:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __call__(self, driver):
        elements = driver.find_elements(By.CLASS_NAME, self.name)

        if len(elements) == self.amount:
            if len(elements) == 0:
                # Если ждали количества элементов 0,
                # ТО вернуть нужно True так как условие выполнено
                return True
            return elements
        else:
            return False


def test_using_lambda(browser):
    # Можно использовать функцию или lambda выражение
    browser.get("https://konflic.github.io/front_example")
    el = WebDriverWait(browser, 2).until(lambda d: d.find_element_by_name("showjsbutton"))
    assert el.text == "Ajax Request"


def test_custom_wait(browser):
    browser.get("https://konflic.github.io/front_example")
    button = browser.find_element_by_name("showjsbutton")
    # Делаем три клика по элементам
    button.click()
    button.click()
    button.click()
    # Ждем 3 секунды пок ана странице не будет 3 элемента
    elements = WebDriverWait(browser, 3).until(amount_of_elements_with_name("target", 3))
    # Выполняем клик по всем элементам
    for el in elements: el.click()
    # Ждем пока не странице не останется один элемент
    elements = WebDriverWait(browser, 2).until(amount_of_elements_with_name("target", 1))
    # Кликаем в единственный элемент в массиве
    elements[0].click()
    # Ждем пока элементов на странице не станет 0
    WebDriverWait(browser, 3).until(amount_of_elements_with_name("target", 0))
