import requests
from bs4 import BeautifulSoup
import json


def get_html(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        "accept": "* / *"
    }

    r = requests.get(url, headers=headers, timeout=0.3)
    # with open("sale_notebook.html", "wb") as f:
    #     f.write(r.content)

    # with open("sale_notebook.html", "rb") as f:
    #     html_content = f.read()

    notebooks = []
    # soup = BeautifulSoup(html_content, "lxml")
    soup = BeautifulSoup(r.content, "lxml")
    table = soup.find("table", class_="goods-list-grouped-table")
    tr = table.findAll("tr", class_="goods-list-header")
    for item in tr[:2]:
        name = item.find("h3").find("span").text.strip()
        link = "https://www.notik.ru" + item.findNext("tr").find("div").findNext("div").find("a").get("href")
        price = item.findNext("tr").findNext("tr").find("td", class_="gltc-cart").find("a").get("ecprice")
        td_params = item.findNext("tr").findNext("tr").findAll("td")
        params = []
        for param in td_params[:7]:
            params.append(param.text.replace("\r", " ").replace("Восстановленный ноутбук", "").replace("  ", " ").replace("  ", " ").strip())
        notebooks.append(
            {
                "Title": name,
                "Link": link,
                "Price": price,
                "Specifications": params
            }
        )
    with open("notebooks.json", "w", encoding="utf-8") as file:
        json.dump(notebooks, file, indent=4, ensure_ascii=False)


def main():
    # get_html("https://www.notik.ru/search_catalog/filter/sales.htm?sortby=price") - all models
    get_html("https://www.notik.ru/search_catalog/filter/sales.htm?srch=true&full=&f28=19293&sortby=price") # - HP models


if __name__ == '__main__':
    main()