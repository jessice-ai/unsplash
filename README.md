# Unsplash: Beautiful Free Images & Pictures

Unsplash api python down free images

#### 克隆项目

```
git clone https://github.com/jessice-ai/unsplash.git
cd unsplash
```

#### Python独立环境构建

```
1、pip install virtualenv #安装
2、virtualenv venv --python=python3.9 #指定版本
3、source venv/Scripts/activate #进入环境
```

安装Scrapy

```
pip install scrapy
```

#### Selenium 自动化网络浏览器交互

```
1、pip install selenium #添加插件
2、https://chromedriver.chromium.org/downloads #选择合适版本,解压目录加入环境变量

注意: chromedriver 版本要与 安装 chrome 浏览器版本匹配

问题: 如果出现不匹配问题

解决:
方式1: chromedriver 版本与 安装 chrome 浏览器版本一致

方式2: 使用 webdriver-manager 管理版本(目前使用的方式)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager(version="93.0.4577.15").install()) #指定版本,
browser.get(url)


```

#### 虚拟代理

```
pip install fake-useragent
```

#### 参数修改

```
1、sun_spider.py #爬虫文件
2、https://api.unsplash.com/search/photos/?client_id=NMf8MYtmGZfrsrogzyg4nmP9h3vjaW0Ouz7_KOnemfo&query=arrow&page=8&per_page=100&order_by=latest #修改对应参数即可
```

#### 运行项目

```
cd spiderProject/
scrapy crawl sun_spider
```

