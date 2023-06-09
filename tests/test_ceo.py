import time

from pages.accordian import AccordianPage
from pages.alerts import Alerts

from pages.demoqa import DemoQA
from pages.browser_tab import BrowserTab

import pytest

def test_navigation(browser):
    ceo_demoqa = DemoQA(browser)

    ceo_demoqa.visit()
    assert browser.title == ceo_demoqa.pageData['title']


@pytest.mark.parametrize('pages', [AccordianPage, Alerts, DemoQA, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)


    page.visit()
    time.sleep(2)
    assert browser.title == page.pageData['title']
