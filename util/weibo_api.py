import logging
from urllib import parse

import requests
from requests.exceptions import Timeout
from config.urls import UID_URL, FANS_NUM_URL, STATUS_DETAIL_URL


def get_uid_from_api(nickname):
    """
    获取uid
    测试网址：http://open.weibo.com/widget/followbutton.php
    请求参数：{nickname : nickname_urlcode}
    示例响应：成功：{code:"A00006",data:2395743084}  获取成功，data为uid
             失败：{code:"A00001"}                  表示没有该用户

    :param nickname: 用户昵称(string)
    :return: 用户uid(string)
    """
    uid_url = UID_URL
    uid_headers = {
        'Referer': 'http://open.weibo.com/widget/followbutton.php',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    nickname_quote_once = parse.quote(nickname)  # 对昵称urlcode编码
    body = {'nickname': nickname_quote_once}
    r = requests.post(uid_url, data=body, headers=uid_headers).json()
    if r['data']:
        return str(r['data'])
    else:
        logging.warning('该用户不存在')
        return None


def get_fans_num_from_api(uid):
    """
    
    :param uid: 账户uid(str)
    :return: 粉丝数(int)
    """
    fans_headers = {
        'Host': 'm.weibo.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    fans_num_url = FANS_NUM_URL.format(id=uid)
    print(fans_num_url)
    try:
        r = requests.get(fans_num_url, headers=fans_headers)
        content = r.json()
    except Timeout:
        logging.warning('Timeout')
        raise
    return content['data']['userInfo']['followers_count']





if __name__ == '__main__':
    # uid = get_uid_from_api('子望')
    # print(uid)
    print(get_fans_num_from_api('2395743084'))
