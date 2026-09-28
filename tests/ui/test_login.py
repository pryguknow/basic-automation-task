

def test_login_user(open_test_page):
    page = open_test_page
    page.fill('input[name="username"]', "tomsmith")
    page.fill('input[name="password"]', "SuperSecretPassword!")
    page.click('button[type="submit"]')

    page.wait_for_url("https://the-internet.herokuapp.com/secure", timeout=5000)
    page.wait_for_selector(".flash.success")

    content = page.content()
    assert "You logged into a secure area!" in content
