from spider.UrlManager import UrlManager
from spider.WeiboDownloader import WeiboDownloader
from spider.WeiboParser import WeiboParser
from spider.WeiboStorer import WeiboStorer


class WeiboSpider:
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = WeiboDownloader()
        self.parser = WeiboParser()
        self.storer = WeiboStorer()

    def crawl(self, uid, start_page=1, include_retweet=True):
        """
        微博爬虫抓取流程
        :param uid: 微博用户id
        :param start_page: 抓取的起始页
        :param include_retweet:
        :return:
        """
        page = start_page
        while True:
            download_url = self.manager.generate_download_url(uid, page)
            weibo_list_json = self.downloader.download_weibo_list(download_url)
            weibo_list = self.parser.parse_weibo_list(weibo_list_json,include_retweet=include_retweet)
            self.storer.store_weibo_to_db(weibo_list)
            # time.sleep(2) 根据实际情况控制抓取间隔
            if weibo_list:
                page += 1
            else:
                break
            if page == 3:
                break


if __name__ == '__main__':
    spider = WeiboSpider()
    # spider.crawl('1921356542')
    # uid = weibo_api.get_uid_from_api('人民日报')
    # print(uid)
    uid = '2803301701'
    spider.crawl(uid)
