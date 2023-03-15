from pages.demoqa import DemoQA

def test_icon(browser):
    demo_page = DemoQA(browser)
    demo_page.visit()
    assert demo_page.exist_icon()
    demo_page.click_on_the_icon()