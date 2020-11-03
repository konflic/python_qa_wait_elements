
def test_check_header(browser):
    browser.implicitly_wait(5)
    browser.get("https://konflic.github.io/front_example/pages/slowlyloading.html")
    browser.find_element_by_id("header")
