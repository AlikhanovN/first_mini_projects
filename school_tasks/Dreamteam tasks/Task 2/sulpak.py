import requests
from bs4 import BeautifulSoup
import csv


def get_data():
    r = requests.get("https://www.sulpak.kg/f/smartfoniy", verify = False)
    soup = BeautifulSoup(r.content, "html.parser")
    global items
    items = soup.findAll("div", class_="goods-tiles")

new_list = []


def parce_data():
    for item in items:
        photo_link = str(item.find("img", class_="image-size-cls"))
        names = item.find("h3", class_="title")
        price = item.find("div", class_="price")
        # descr = item.find("div", class_="product_text pull-left")
        new_list.append({
            "Photo link" : photo_link[photo_link.find("src") + 5:photo_link.rfind('title') - 2],
            "Name" : names.get_text(),
            "Price" : price.get_text(),

        })


def save_data():
    with open('sulpak_for_bot.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=["Photo link", "Name", "Price"])
        writer.writeheader()
        writer.writerows(new_list)


get_data()
parce_data()
save_data()
