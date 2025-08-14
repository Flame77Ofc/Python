import requests
from bs4 import BeautifulSoup
from time import sleep


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


def scraping(site: str):
    r = requests.Session().get(site, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    # "https://www.booking.com/"
    # box = soup.find("div", attrs={"class": "dec8e1cdb2 false"})
    # countries = box.find_all("a")
    # for country in countries:
    #     country_name = country.getText()
    #     country_link = country["href"]

    #     yield f"Nome: {country_name} | Link: {country_link}"



    # https://www.booking.com/searchresults.html?aid=304142&label=gen173nr-10CAEoggI46AdIM1gEaCCIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4AsTzz8QGwAIB0gIkYzUxYTExYWItNzdlZi00Y2MzLTgyYzQtZjIzZWQxNzllM2Yz2AIB4AIB&dest_id=-671824&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0
    # sections = soup.find_all("div", attrs={"role": "listitem"})
    # for section in sections:
    #     name = section.find("a", attrs={"class": "bd77474a8e"}).getText().strip()
    #     link = section.find("a", attrs={"class": "bd77474a8e"}).get("href")

    #     yield f"Nome: {name} \nLink: {link}\n{"-"*30}\n"



    # https://www.realtor.com/realestateandhomes-search/Minneapolis_MN/show-open-house/sby-5
    # hotels = soup.find_all("div", attrs={"class": "s1tw718u atm_wq_kb7nvz dir dir-ltr"})
    # for hotel in hotels:
    #     yield hotel




# for item in scraping("https://www.booking.com/"):
#     print(item)

# for item in scraping("https://www.booking.com/searchresults.html?aid=304142&label=gen173nr-10CAEoggI46AdIM1gEaCCIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4AsTzz8QGwAIB0gIkYzUxYTExYWItNzdlZi00Y2MzLTgyYzQtZjIzZWQxNzllM2Yz2AIB4AIB&dest_id=-671824&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0"):
#     print(item)

# for item in scraping("https://www.airbnb.com.br/"):
#     print(item)
