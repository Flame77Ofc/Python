# # Formas de exibição
# # 1. .locator('elemento') -> Seleciona o elemento especificado
# message = page.locator('.HomepageHero_heading__Nj93Y')
# print(message.inner_text())

# message = page.locator('xpath=//*[@id="__next"]/div/div/main/div/div/div[1]/section[1]/header/h1')
# print(message.inner_text())


# # 2. .query_selector('elemento') -> Seleciona o elemento especificado
# message = page.query_selector('.HomepageHero_heading__Nj93Y')
# print(message.inner_text())

# message = page.query_selector('xpath=//*[@id="__next"]/div/div/main/div/div/div[1]/section[1]/header/h1')
# print(message.inner_text())


# # 3. .query_selector_all('elemento') -> Seleciona todos os elementos após o elemento especificado
# # .get_attribute('attribute') -> Pega atributos.
# title = page.locator('h1')
# print(title.get_attribute('class'))


# # .fill: preenche algo, como um formulário.
# page.goto('https://www.instagram.com')
# user = page.fill('xpath=//*[@id="loginForm"]/div[1]/div[1]/div/label/input', "username")
# password = page.fill('xpath=//*[@id="loginForm"]/div[1]/div[2]/div/label/input', "password")


# # .click: Clica em algo, como um botão.
# page.goto('https://neal.fun/stimulation-clicker/')
# click = page.click('//*[@id="__layout"]/div/div/div[4]/div/div[1]/div/button')
# clicks = page.locator('xpath=//*[@id="__layout"]/div/div/div[4]/div/div[2]/div/div/span').inner_text()

# print(f'Cliques: {clicks}')


# # .press('elemento', 'Enter') -> Dá um enter ná pagina.
# page.press('xpath=//*[@id="APjFqb"]', 'Enter')


# # .screenshot(path="img.png") -> Salva um print do site em um arquivo.
# page.scr
# eenshot(path="screenshot.png")

# # .wait_for_selector('selector') -> Espera até um elemento ser carregado pela página.
# esperar = page.wait_for_selector('xpath=//*[@id="__next"]/div/div/main/div/div/div[1]/section[1]/header/h1')


# # .wait_for_timeout(ms) -> Espera por ms.
# page.wait_for_timeout(10000)


# Criar um html local
# html = """<div>Hello, World!</div>"""
# box = page.locator('div')
# print(box.inner_text())
