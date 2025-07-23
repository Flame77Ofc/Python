"""
Este programa lê e retorna os comentários de uma URL especificada do YouTube.
Como funciona
O playwright será responsável por abrir uma janela do chrome.
Tudo que você precisa fazer é rolar os comentários.
Quanto mais comentários na tela = mais comentários retornados.
O programa retorna os comentários lidos no terminal e num arquivo comments.txt.
"""
from playwright.sync_api import sync_playwright


def read_comments(video: str):
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(video)

            page.wait_for_selector("#content-text")
            page.wait_for_timeout(5000)

            comments = page.query_selector_all("#content-text")
            for comment in comments:
                yield f"{comment.inner_text()}\n"

                if comment is not None:
                    with open("comments.txt", "a+", encoding="utf-8") as f:
                        f.write(f"<------------------>\n{
                            str(comment.inner_text())}\n\n")

    except Exception as error:
        yield f"Erro: {error}"


if __name__ == "__main__":
    for item in read_comments("https://www.youtube.com/watch?v=3LHSyha0xN0"):
        print(item)
