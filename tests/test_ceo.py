from pages.demoqa import DemoQA


def test_navigation(browser):
    ceo_demoqa = DemoQA(browser)

    ceo_demoqa.visit()
    assert browser.title == ceo_demoqa.pageData['title']