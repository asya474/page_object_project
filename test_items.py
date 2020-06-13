import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_existbutton(browser):
    browser.get(link)
    
    assert browser.find_element_by_class_name("btn-add-to-basket"), "Button not find"
    time.sleep(30)