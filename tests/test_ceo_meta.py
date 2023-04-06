import time

from pages.accordian import AccordianPage
from pages.alerts import Alerts
from pages.demoqa import DemoQA
from pages.browser_tab import BrowserTab

import pytest

@pytest.mark.parametrize('pages', [AccordianPage, Alerts, DemoQA, BrowserTab])
def test_check_ceo_meta(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)


    assert page.head_meta.exist()
    assert page.head_meta.get_dom_attribute('name') == 'viewport'
    assert page.head_meta.get_dom_attribute('content') == 'width=device-width,initial-scale=1'