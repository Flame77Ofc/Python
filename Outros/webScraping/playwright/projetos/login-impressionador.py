from playwright.sync_api import sync_playwright

nomes = ["Mario", "Bruno", "Carla", "Felipe", "Gabriela", "Henrique", "Isabel", "João"]

for i in range(len(nomes)):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.hashtagtreinamentos.com/curso-de-excel-online?utm_source=site&utm_medium=header&utm_content=link-header-cursos&utm_campaign=treinamento&conversion=lcto-lex39-fev26')

        name = page.fill('xpath=//*[@id="firstname"]', nomes[i])
        email = page.fill('xpath=//*[@id="email"]', 'flame77ofc@gmail.com')
        whatsapp = page.fill('xpath=//*[@id="phone"]', '47984077762')

        submit = page.click('xpath=//*[@id="_form_178_submit"]')


        if page.query_selector('xpath=//*[@id="firstname"]'):
            print('Concluído')
        else:
            print('Erro')
