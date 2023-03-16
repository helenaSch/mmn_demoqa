from pages.demoqa import DemoQA

def test_icon(browser):
    demo_page = DemoQA(browser)
    demo_page.visit()
    demo_page.click_on_the_icon()
    assert demo_page.exist_icon()
    assert demo_page.equal_url()
