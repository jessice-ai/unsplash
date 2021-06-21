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
2、https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_win32.zip #解压目录加入环境变量
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

