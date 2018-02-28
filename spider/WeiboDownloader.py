import logging

import requests


class WeiboDownloader:
    def download_weibo_list(self, download_url):
        """
        请求微博api，返回请求结果
        :param download_url: 微博api地址
        :return: json格式的请求结果
        """
        download_header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
        r = None
        try:
            r = requests.get(download_url, headers=download_header, timeout=5)
        except Exception as e:

            logging.warning(e)
        return r.json()


