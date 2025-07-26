from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demoqa.com/automation-practice-form')

    first_name = page.fill('xpath=//*[@id="firstName"]', 'Flame')
    last_name = page.fill('xpath=//*[@id="lastName"]', 'Snow')
    email = page.fill('xpath=//*[@id="userEmail"]', 'flamesnow@gmail.com')

    gender = page.click('xpath=//*[@id="gender-radio-1"]')

    phone_number = page.fill('xpath=//*[@id="userNumber"]', 5577638393)
    birth = page.query_selector('xpath=//*[@id="dateOfBirthInput"]')
    print(birth.inner_text())
