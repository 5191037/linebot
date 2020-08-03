import time
import re
import requests
import sys
from bs4 import BeautifulSoup
from pymongo import MongoClient
from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""
攻略情報ページの一覧を回収するソースコード
"""


def kamigame(URL):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(URL)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    driver.quit()

    i = 0
    site_info = soup.select('#top_mobile_game_list')
    mobile = site_info[0].find_all('a')

    for info in tqdm(mobile):
        name = info.get_text()
        url = ("https://kamigame.jp" + info.get('href'))
        image = ("https://kamigame.jp" + info.find('img').get('src'))
        # print(name, url, image + '\n')
        my_dict = {'_id': i, 'name': name, 'url': url, 'image': image}
        collection.insert_one(my_dict)
        i += 1

    site_info = soup.select('#top_consumer_game_list')
    consumer = site_info[0].find_all('a')

    for info in tqdm(consumer):
        name = info.get_text()
        url = ("https://kamigame.jp" + info.get('href'))
        image = ("https://kamigame.jp" + info.find('img').get('src'))
        # print(name, url, image + '\n')
        my_dict = {'_id': i, 'name': name, 'url': url, 'image': image}
        collection.insert_one(my_dict)
        i += 1

    site_info = soup.select('#latest_news_list')
    news = site_info[0].find_all('a')

    for info in tqdm(news):
        name = info.find(class_='txt--title').get_text() + "【News】"
        url = info.get('href')
        image = info.find(class_='vertical-list__img-wrap').find('img').get('src')
        # print(name, url, image + '\n')
        my_dict = {'_id': i, 'name': name, 'url': url, 'image': image}
        collection.insert_one(my_dict)
        i += 1


if __name__ == "__main__":
    args = sys.argv

    if len(args) != 2:
        print("Usage:python bot.py URL")
        sys.exit(1)

    URL = args[1]
    p = re.compile(r'^(http|https)://[a-z0-9][a-z0-9\-\._]*\.[a-z]+'r'(?:[0-9]+)?(?:/.*)?$')

    if not p.match(URL):
        print("invaid argument.")
        sys.exit(2)

    client = MongoClient('localhost', 27017)
    db = client.scraping
    collection = db.bot_fe

    kamigame(URL)
