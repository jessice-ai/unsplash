import scrapy
# from fake_useragent import UserAgent
from urllib.parse import urlparse
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
import os


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
    keyword = "Animals"
    start_urls = [
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=11&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=12&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=13&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=14&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=15&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=16&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=17&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=18&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=19&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=20&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=21&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=22&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=23&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=24&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=25&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=26&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=27&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=28&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=29&per_page=30&order_by=latest",
        "https://api.unsplash.com/search/photos?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=" + keyword + "&page=30&per_page=30&order_by=latest",
    ]
    headers = {
#         'User-Agent': UserAgent().chrome,
      'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        # Host 使用第一个网址中的全域名,如果手动写，注意 aaa.com 与 www.aaa.com 解析后的IP地址不同情况
        # Host 是 HTTP / 1.1 必须包含参数,作用:指定用户要访问的域名
        # "Host": "%s:8091" % urlparse(start_urls[0]).netloc,
        "Host": "%s" % urlparse(start_urls[0]).netloc,
    }

    def start_requests(self):
        for url in self.start_urls:
            # 说明 don't_filter=True Scrapy内置了重复过滤功能,设置为True表示,不过滤重复请求
            yield scrapy.Request(url, callback=self.parse, headers=self.headers, dont_filter=True)

    def create_csv(self):
        with open("test.csv", 'w', encoding="utf-8", newline='') as csvfile:
            csv_write = csv.DictWriter(csvfile, self.field_order)
            csv_write.writeheader()
            # csv_write.writerow(dict(zip(self.field_order, ["李6四", 10, "男"])))
            # csv_write.writerow(dict(zip(self.field_order, ["李6四3", 10, "男"])))
            # csv_write.writerow(dict(zip(self.field_order, ["李6四4", 10, "男"])))
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
            # writer.writerow(dict(zip(field_order, ["李四", 10, "男"])))
            # writer.writerow(dict(zip(field_order, ["王五", 30, "男"])))

    def parse(self, response):
        data = response.text
        dict1 = json.loads(data)
        i = 1
        for item in dict1['results']:
            arr = []
            # print(item)
            # print(item["id"]) #ID
            # print(item["alt_description"]) #描述
            tag_str = tag_str_sign = ""

            for tag in item["tags"]:
                tag_str += tag_str_sign + tag["title"];
                tag_str_sign = ","

            alt_description = item["id"]
            if item["alt_description"] is not None:
                alt_description = item["alt_description"]

            # print(item.get('urls').get('full'))
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

            # 自动模拟浏览器下载
            # browser = webdriver.Chrome()
            browser = webdriver.Chrome(ChromeDriverManager(version="93.0.4577.15").install())
            browser.get(url)
            # 追加内容到CSV文件
            write_csv(arr)
            i += 1
        pass
