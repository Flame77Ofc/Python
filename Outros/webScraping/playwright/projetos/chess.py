from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://chess.com/')

    login = page.click('xpath=//*[@id="sb"]/div[3]/a[9]')

    username = page.fill('xpath=//*[@id="login-username"]', 'gabrielgoulartbnu@gmail.com')
    password = page.fill('xpath=//*[@id="login-password"]', 'missme1406')
    button = page.click('xpath=//*[@id="login"]')

    jogar = page.click('xpath=/html/body/div[1]/div[2]/div[4]/div[1]/div/a[1]')

    page.wait_for_timeout(10000000)

