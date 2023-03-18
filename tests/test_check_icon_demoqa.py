from pages.demoqa import DemoQA


def test_icon(browser):
    demo_page = DemoQA(browser)


    demo_page.visit()
    demo_page.icon.click()
    assert demo_page.icon.exist()
    assert demo_page.equal_url()
