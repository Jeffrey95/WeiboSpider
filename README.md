# 新浪微博爬虫
## 简介
一个基于requests、SQLAlchemy的新浪微博爬虫，使用python3编写。最近正在重构以前写的代码。目前实现了对微博m站的api进行简单的封装，单线程爬取微博，存储到Mysql数据库。之后需要采用多线程、异步等方式提高抓取效率以及完善相应的反爬措施。

## 结构
```
├── README.md
├── config    # 爬虫配置
│   ├── __init__.py
│   └── urls.py
├── db
│   ├── TableDef.py                # 数据库表定义
│   └── __init__.py
├── requirement.txt
├── spider
│   ├── UrlManager.py              # url生成类
│   ├── WeiboDownloader.py         # 微博下载类
│   ├── WeiboParser.py             # 微博解析类
│   ├── WeiboSpider.py             # 微博爬虫类
│   ├── WeiboStorer.py             # 微博数据存储类
│   └── __init__.py
└── util                           # 工具库
    ├── __init__.py
    ├── clean_tool.py
    └── weibo_api.py
```

## 数据库字段
```
+----------------+-----------------------------+
| column_name    | column_comment              |
+----------------+-----------------------------+
| weibo_id       | 微博id                       |
| bid            | 微博id                       |
| nickname       | 用户昵称                      |
| created_at     | 微博发布时间                   |
| is_retweet     | 是否转发                      |
| title          | 微博标题                      |
| text           | 微博文本                      |
| source         | 微博来源                      |
| page_exist     | 是否有外链                    |
| pic_exist      | 是否有图片                    |
| has_cleaned    | 数据是否已经清洗               |
| is_long_text   | 是否长微博                    |
| crawl_complete | 是否已获取微博全文             |
```

## 安装

1. 安装依赖库
    ```bash
    $ pip install -r requirement.txt
    ```
2. 安装mysql

3. 配置config/urls.py文件
    * mysql
    ```
    # 将user,password,datebase按你的实际情况更改

    mysql+pymysql://user:password@localhost:3306/datebase?charset=utf8mb4

    # 如user为root,password为mypasswd,database为weibotest，则配置为:

    mysql+pymysql://root:mypasswd@localhost:3306/testweibo?charset=utf8mb4
    ```
    * 其他数据库  
    参考[SQLAlchemy文档](http://docs.sqlalchemy.org/en/latest/dialects/index.html)，选择你的数据库，并找到相应的Connecting方式

## 使用
1. 获取uid
    * 手动获取
        1. 访问目标用户的网页版主页，这里以[中山大学](https://weibo.com/u/1892723783?refer_flag=0000015010_&from=feed&loc=nickname&is_all=1)为例
        ![中山大学](https://wx1.sinaimg.cn/large/728592fegy1fowha1a247j20yx07ago9.jpg)
        图中红标部分即为用户id、uid
        2. 访问目标用户的m站主页，这里以[中山大学 手机端网站](https://m.weibo.cn/u/1892723783?uid=1892723783&luicode=10000011&lfid=100103type%3D17%26q%3D%E4%B8%AD%E5%B1%B1%E5%A4%A7%E5%AD%A6&featurecode=20000320)为例
        ![image](https://ws2.sinaimg.cn/large/728592fegy1fowhisq5p2j210f07t76b.jpg)
        红色圈中部分即为用户uid
    * 程序获取  
        代码中的util/weibo_api里封装了`get_uid_from_api`函数
        可以通过以下的调用方式获取uid
        ```python
        get_uid_from_api('目的用户昵称')
        ```
2. 初始化数据库
    1. 登录mysql
    ```
    $ mysql -uroot -p
    ```
    2. mysql中创建databes;
    ```sql
    mysql> create database weibotest
    ```
    3. 运行db/TableDef.py来创建table
    ```
    $ cd db/
    $ python3 ./TableDef.py
    ```

3. 抓取微博
    ```python
    from spider.WeiboSpider import WeiboSpider

    spider = WeiboSpider()
    uid = get_uid_from_api('目的用户昵称')
    # 这里uid可自行构造
    spider.crawl(uid)
    ```
    crawl函数的原型为：
    ```python
    def crawl(self, uid, start_page=1, include_retweet=True)
    ```
    默认情况下从page=1开始抓取，如果遇到异常导致抓取中断，可自定义start_page来继续抓取。
    include_retweet表示抓取转发微博。如不需要，设置为False即可。
