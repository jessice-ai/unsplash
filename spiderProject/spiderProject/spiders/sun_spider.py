import scrapy
# from fake_useragent import UserAgent
from urllib.parse import urlparse
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
import os
import pdb


def write_csv(arr):
    with open("test.csv", 'a', encoding="utf-8", newline='') as csvfile:
        csv_write = csv.writer(csvfile)
        csv_write.writerow(arr)


class SunSpiderSpider(scrapy.Spider):
    name = 'sun_spider'
    sun_write = False
    writer = ""
    field_order = ["Filename", 'Description', 'Keywords', 'Categories', 'Mature content', 'Editorial']
    allowed_domains = ['unsplash.com']
    keyword = "Wildlife"
    order_by = "latest"
    start_urls = [
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=1&per_page=30&order_by=" + order_by,
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=2&per_page=30&order_by=" + order_by,
        # "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=3&per_page=30&order_by="+order_by,
        # "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=4&per_page=30&order_by="+order_by,
        # "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=5&per_page=30&order_by="+order_by,
        # "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=6&per_page=30&order_by="+order_by,
        # "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=7&per_page=30&order_by="+order_by,
        # "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=8&per_page=30&order_by="+order_by,
        # "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=9&per_page=30&order_by="+order_by,
        # "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=10&per_page=30&order_by="+order_by,
    ]
    headers = {
        #         'User-Agent': UserAgent().chrome,
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        # Host ????????????????????????????????????,???????????????????????? aaa.com ??? www.aaa.com ????????????IP??????????????????
        # Host ??? HTTP / 1.1 ??????????????????,??????:??????????????????????????????
        # "Host": "%s:8091" % urlparse(start_urls[0]).netloc,
        "Host": "%s" % urlparse(start_urls[0]).netloc,
    }

    def start_requests(self):
        for url in self.start_urls:
            # ?????? don't_filter=True Scrapy???????????????????????????,?????????True??????,?????????????????????
            yield scrapy.Request(url, callback=self.parse, headers=self.headers, dont_filter=True)

    def create_csv(self):
        with open("test.csv", 'w', encoding="utf-8", newline='') as csvfile:
            csv_write = csv.DictWriter(csvfile, self.field_order)
            csv_write.writeheader()
            # csv_write.writerow(dict(zip(self.field_order, ["???6???", 10, "???"])))
            # csv_write.writerow(dict(zip(self.field_order, ["???6???3", 10, "???"])))
            # csv_write.writerow(dict(zip(self.field_order, ["???6???4", 10, "???"])))
            CategotyList = [
                "Abstract",
                "Miscellaneous",
                "Animals/Wildlife",
                "Nature",
                "Backgrounds/Textures",
                "Objects",
                "Beauty/Fashion",
                "Parks/Outdoor",
                "Buildings/Landmarks",
                "People",
                "Business/Finance",
                "Religion",
                "Celebrities",
                "Science",
                "Education",
                "Signs/Symbols",
                "Food and Drink",
                "Sports/Recreation",
                "Healthcare/Medical",
                "Technology",
                "Holidays",
                "The Arts",
                "Industrial",
                "Transportation",
                "Interiors",
                "Vintage",
            ]
            # writer.writerow(dict(zip(field_order, ["??????", 10, "???"])))
            # writer.writerow(dict(zip(field_order, ["??????", 30, "???"])))

    def parse(self, response):
        data = response.text
        dict1 = json.loads(data)
        i = 1
        for item in dict1['results']:
            arr = []
            # print(item)
            # print(item["id"]) #ID
            # print(item["alt_description"]) #??????
            tag_str = tag_str_sign = ""

            for tag in item["tags"]:
                tag_str += tag_str_sign + tag["title"];
                tag_str_sign = ","

            # alt_description = item["id"]
            # print(tag)
            alt_description = item["alt_description"]
            url = item.get('urls').get('full')

            if item["alt_description"] is not None:
                arx = len(alt_description.split(" "))
                if arx >= 5:
                    print(f'----------------Tag:{alt_description}----------------')
                    message = alt_description
                    t_url = item.get('urls').get('full')
                    t = t_url.index('ixid=')
                    t_url = t_url[:t]
                    name = item.get('user').get('name')
                    name = name.replace(" ", '-')
                    url = t_url + '&dl=' + alt_description + '.jpg'
                    tag_str = tag_str + ',' + alt_description.replace(" ", ",")
                    arr.append(alt_description + '.jpg')
                    arr.append(alt_description)
                    arr.append(tag_str)
                    arr.append("")
                    arr.append('No')
                    arr.append('No')

                    if not self.sun_write:
                        self.create_csv()
                        self.sun_write = True

                    # ???????????????????????????
                    # browser = webserver.Chrome()
                    option = webdriver.ChromeOptions()
                    option.add_experimental_option("detach", True)

                    browser = webdriver.Chrome(ChromeDriverManager(version="93.0.4577.15").install(),options=option)
                    browser.get(url)
                    # ???????????????CSV??????
                    write_csv(arr)
                    i += 1
        pass
