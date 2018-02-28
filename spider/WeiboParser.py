from db.TableDef import Weibo
from util.clean_tool import convey_time, clean_text, extract_title


class WeiboParser:
    def parse_weibo_list(self, weibo_list_json, include_retweet=True):
        """
        解析每一页的json响应内容
        示例数据：https://m.weibo.cn/api/container/getIndex?containerid=2304132803301701_-_WEIBO_SECOND_PROFILE_WEIBO&page=1
        :param weibo_list_json: 抓取下来每一页的json响应内容
        :param include_retweet: 是否返回转发的微博，默认为True
        :return: weibo_result_list解析出的微博结果列表
        """

        if weibo_list_json is None:
            return None
        weibo_result_list = []
        weibos = weibo_list_json['data']['cards']

        for weibo_item in weibos:
            weibo_type = weibo_item.get('card_type')
            if weibo_type == 58:
                return None  # 无微博
            if weibo_type != 9:  # card_type=9的才是微博
                continue

            blog_content = weibo_item.get('mblog')
            weibo_id = blog_content.get('id')
            bid = blog_content.get('bid')
            nickname = blog_content.get('user').get('screen_name')
            created_at = blog_content.get('created_at')
            created_at = convey_time(created_at)
            is_retweet = 'retweeted_status' in blog_content
            text = blog_content.get('text')
            text = clean_text(text)
            title = extract_title(text)
            source = blog_content.get('source')
            is_long_text = blog_content['isLongText']
            page_exist = 'page_info' in blog_content
            pic_exist = 'pics' in blog_content
            crawl_complete = not is_long_text
            if not include_retweet and is_retweet:
                continue
            weibo = Weibo(weibo_id=weibo_id, bid=bid, nickname=nickname, created_at=created_at, title=title,
                          text=text, is_retweet=is_retweet, source=source, page_exist=page_exist,
                          pic_exist=pic_exist, has_cleaned=False, is_long_text=is_long_text,
                          crawl_complete=crawl_complete)
            weibo_result_list.append(weibo)
        return weibo_result_list
