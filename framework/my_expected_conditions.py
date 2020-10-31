class my_custom_condidion:

    def __init__(self, locator, amount):
        self.locator = locator
        self.amount = amount

    def __call__(self, driver):
        return len(driver.find_elements(*self.locator)) == self.amount
