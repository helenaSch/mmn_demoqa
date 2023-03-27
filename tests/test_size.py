import time

from pages.demoqa import DemoQA


def test_size(browser):
    s_demoqa = DemoQA(browser)

    s_demoqa.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)