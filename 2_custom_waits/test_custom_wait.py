import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def amount_of_elements(selector, amount):
    def __predicate(driver):

        elements = driver.find_elements(By.CSS_SELECTOR, selector) # Безопасно ищу все элементы на странице

        if len(elements) == amount: # Если количество элементов совпало с ожидаемым
            if amount == 0:
                return True # Если ждали количества элементов 0, То вернуть True так как условие выполнено, а 0 будет воспринят как False

            return elements if amount > 1 else elements[0] # Возвращаю все элементы, либо один если искали 1

        return False

    return __predicate


AJAX_EXAMPLE = "https://konflic.github.io/examples/pages/ajax.html"


def test_custom_wait(browser):
    browser.get(AJAX_EXAMPLE)
    button = browser.find_element(By.NAME, "showjsbutton")

    # Берем случайное количество действий для теста
    test_amount = random.randint(3, 8)

    # Делаем клики в установленном выше количестве
    for _ in range(test_amount): button.click()

    # Ждем пока не появится нужное количество элементов
    elements = WebDriverWait(browser, 5).until(amount_of_elements(".target", test_amount))

    # Выполняю клик по всем кроме одного элемента
    for el in elements[:-1]: el.click()

    # Жду пока не странице не останется один элемент
    last_element = WebDriverWait(browser, 2).until(amount_of_elements(".target", 1))

    # Кликаем в единственный элемент в массиве
    last_element.click()

    # Жду пока элементов на странице не станет 0
    WebDriverWait(browser, 3).until(amount_of_elements(".target", 0))
