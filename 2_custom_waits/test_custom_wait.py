import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class amount_of_elements_with_class_name:
    def __init__(self, class_name, amount):
        self.class_name = class_name
        self.amount = amount

    def __call__(self, driver):
        # Безопасно ищу все элементы на странице
        elements = driver.find_elements(By.CLASS_NAME, self.class_name)
        # Если количество элементов сопало с ожидаемым
        if len(elements) == self.amount:
            # Если ждали количества элементов 0,
            # То вернуть True так как условие выполнено, а 0 будет воспринят как False
            if len(elements) == 0: return True
            # Возвращаю все элементы, либо один
            return elements if self.amount > 1 else elements[0]
        else:
            # Если кол-во элементов не равно ожидаемому возвращаю False
            return False


AJAX_EXAMPLE = "https://konflic.github.io/examples/pages/ajax.html"


def test_using_lambda(browser):
    # Можно использовать функцию или lambda выражение
    browser.get(AJAX_EXAMPLE)
    el = WebDriverWait(browser, 2).until(lambda driver: driver.find_element_by_name("showjsbutton"))
    assert el.text == "Ajax Request"


def test_custom_wait(browser):
    browser.get(AJAX_EXAMPLE)
    button = browser.find_element_by_name("showjsbutton")

    # Берем случайное количество действий для теста
    test_amount = random.randint(3, 8)

    # Делаем клики в установленном выше количесте
    for _ in range(test_amount):
        button.click()

    # Ждем пока не появится нужное количество элементов
    elements = WebDriverWait(browser, 5).until(amount_of_elements_with_class_name("target", test_amount))

    # Выполняю клик по всем кроме одного элемента
    elements.pop()
    for el in elements: el.click()

    # Жду пока не странице не останется один элемент
    last_element = WebDriverWait(browser, 2).until(amount_of_elements_with_class_name("target", 1))

    # Кликаем в единственный элемент в массиве
    last_element.click()

    # Жду пока элементов на странице не станет 0
    WebDriverWait(browser, 3).until(amount_of_elements_with_class_name("target", 0))
