from locator.SlowPage import SlowPage
from locator.MainPage import MainPage
from framework import helpers


def test_check_header(browser):
    browser.get("https://konflic.github.io/front_example/slowlyloading.html")
    element = helpers.wait_for_element_locates(browser, SlowPage.HEADER, timeout=4)


def test_featured_products_amount(browser):
    browser.get("http://localhost")
    helpers.wait_for_elements_amount_presence(browser, MainPage.PRODUCT_THUMB, amount=4)
    thumb = helpers.my_find_element(browser, MainPage.PRODUCT_THUMB)
    assert "MacBook" in thumb.text
