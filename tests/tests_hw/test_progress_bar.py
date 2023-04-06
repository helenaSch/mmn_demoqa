import time

from pages.progress_bar import ProgressBar



def test_progress_bar(browser):
    bar_page = ProgressBar(browser)


    bar_page.visit()
    time.sleep(2)
    bar_page.btn_pb.click()
    time.sleep(5.1)
    bar_page.btn_pb.click()
    assert bar_page.running_line.get_dom_attribute('aria-valuenow') == '51'