import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.6422.113 Safari/537.36 "
        "Edg/125.0.2535.67"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
        "application/signed-exchange;v=b3;q=0.7"
    ),
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Ch-Ua": (
        '"Chromium";v="125", "Microsoft Edge";v="125", '
        '"Not.A/Brand";v="24"'
    ),
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "DNT": "1",
    "TE": "trailers"
}


def main():
    class MegaScraping:
        def __init__(self, site: str):
            self.site = site

            self.r = requests.Session().get(self.site, headers=headers)
            self.soup = BeautifulSoup(self.r.content, "html.parser")
            self.error = None

            try:
                self.r = requests.Session().get(self.site, headers=headers)
                self.soup = BeautifulSoup(self.r.content, "html.parser")
            except requests.exceptions.ConnectionError as conn_error:
                self.error = f"Erro de conexão: {conn_error}"
            except requests.exceptions.InvalidURL as inv_URL:
                self.error = f"URL Inválida: {inv_URL}"
            except Exception as e:
                self.error = f"Erro inesperado: {e}"


        def verify_connection_status(self):
            if self.error:
                return self.error

            return (
                f"Status de Requisição: {self.r.status_code}\n"
                f"Ok: {self.r.ok}"
                    )

        def get_requests_content(self):
            if self.error:
                self.error

            content = self.r.content
            return content


        def get_requests_text(self):
            if self.error:
                self.error

            text = self.r.text
            return text


        def get_structured_html(self):
            if self.error:
                self.error

            structured_html = self.soup.prettify()
            return structured_html


        def find_title(self):
            if self.error:
                return self.error

            title = self.soup.find("title")
            return title


        def find_titles_hierarchies(self, get_text: bool, strip: bool):
            if self.error:
                yield self.error
                return None

            if not get_text and strip:
                yield "Impossível eliminar espaços em branco sem procurar pelo texto."
                return None

            if not get_text and not strip:
                h1_title = self.soup.find("h1")

                yield f"TÍTULO H1: {h1_title}"
                for i in range(2, 7):
                    for title in self.soup.find_all(f"h{i}"):
                        yield title

            if get_text and not strip:
                h1_title = self.soup.find("h1")

                yield f"TÍTULO H1: {h1_title.getText()}"
                for i in range(2, 7):
                    for title in self.soup.find_all(f"h{i}"):
                        yield title.getText()

            if get_text and strip:
                h1_title = self.soup.find("h1")

                yield f"TÍTULO H1: {h1_title.getText().strip()}"

                for i in range(2, 7):
                    yield f"\nTÍTULO H{i}:"
                    for title in self.soup.find_all(f"h{i}"):
                        yield title.getText().strip()


        def find_paragraphs(self, get_text: bool, strip: bool):
            if self.error:
                yield self.error
                return None

            if not get_text and strip:
                yield "Impossível eliminar espaços em branco sem procurar pelo texto."
                return None

            paragraphs = self.soup.find_all("p")
            if not get_text and not strip:
                for paragraph in paragraphs:
                    yield paragraph

            if get_text and not strip:
                for paragraph in paragraphs:
                    yield paragraph.getText()

            if get_text and strip:
                for paragraph in paragraphs:
                    yield paragraph.getText().strip()


        def find_links(self):
            if self.error:
                yield self.error
                return None

            links = self.soup.find_all("a")
            yield "Links:"
            for link in links:
                if link.has_attr("href"):
                    yield link["href"]


        def find_images(self):
            if self.error:
                yield self.error
                return None

            images = self.soup.find_all("img")
            for image in images:
                if image.has_attr("src"):
                    yield image["src"]
                else:
                    yield image


    webscraper_io = MegaScraping("https://webscraper.io/test-sites/e-commerce/allinone")
    webscraper_io.verify_connection_status()

    for item in webscraper_io.find_links():
        print(item)

if __name__ == "__main__":
    main()
