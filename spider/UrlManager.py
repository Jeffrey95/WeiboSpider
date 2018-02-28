from config.urls import WEIBO_LIST_URL


class UrlManager:
    def generate_download_url(self, uid, page):
        download_url = WEIBO_LIST_URL.format(id=uid, page_num=page)
        return download_url
