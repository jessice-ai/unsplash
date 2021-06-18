import scrapy
from fake_useragent import UserAgent
from urllib.parse import urlparse
import json
from selenium import webdriver


class SunSpiderSpider(scrapy.Spider):
    name = 'sun_spider'
    allowed_domains = ['unsplash.com']
    start_urls = ['https://api.unsplash.com/search/photos/?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=love&page=2&per_page=100&order_by=latest']
    headers = {
        'User-Agent': UserAgent().chrome,
        "Content-Type": "application/json",
        # Host 使用第一个网址中的全域名,如果手动写，注意 aaa.com 与 www.aaa.com 解析后的IP地址不同情况
        # Host 是 HTTP / 1.1 必须包含参数,作用:指定用户要访问的域名
        #"Host": "%s:8091" % urlparse(start_urls[0]).netloc,
        "Host": "%s" % urlparse(start_urls[0]).netloc,
    }
    def start_requests(self):
        for url in self.start_urls:
            # 说明 dont_filter=True Scrapy内置了重复过滤功能,设置为True表示,不过滤重复请求
            yield scrapy.Request(url,callback=self.parse, headers=self.headers,dont_filter=True)

    def parse(self, response):
        data = response.text
        dict1 = json.loads(data)
        i=1
        for item in dict1['results']:
            # print(item)
            # print(item["id"]) #ID
            #print(item["alt_description"]) #描述
            # print(item["tags"])
            alt_description = item["id"]
            if item["alt_description"]!=None:
                alt_description = item["alt_description"]

            # print(item.get('urls').get('full'))
            t_url = item.get('urls').get('full')
            t = t_url.index('ixid=')
            t_url = t_url[:t]
            name = item.get('user').get('name')
            name = name.replace(" ", '-')
            url = t_url + '&dl=' + alt_description + '.jpg'

            # 自动模拟浏览器下载
            browser = webdriver.Chrome()
            browser.get(url)
            # print(url)
            print(i)
            i+=1

        pass
