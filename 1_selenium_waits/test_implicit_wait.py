def test_check_header(browser):
    browser.get("http://0.0.0.0:8000/else.html")
    # browser.implicitly_wait(5)
    browser.find_element_by_id("header")
