import re
from datetime import datetime, timedelta

title_pattern = re.compile('(?<=【).*(?=】)')


def extract_title(text):
    """
    使用正则表达式text里匹配title
    例如：
    text:【5月春色不错过，3000万粉丝不辜负！】第一届#新闻晨报粉丝节#将于5月27日至5月29日登陆上海锦江乐园
    title: 5月春色不错过，3000万粉丝不辜负！
    :param text: 微博文本
    :return: 如果能匹配到，返回匹配文本。否则，返回None
    """
    title = None
    title_result = title_pattern.findall(text)
    if title_result:
        title = title_result[0]
    return title


def clean_text(text):
    """
    清洗微博文本。目前没有出去微博中的html标签
    :param text: 微博文本。
    :return: text 清洗后的文本
    """
    text = re.sub('\u200b', '', text)
    return text


def convey_time(created_at):
    """
    时间格式：
    24小时以内的：
    xx分钟前
    xx小时前

    24小时~前一天00:00

    02-12
    2017-02-12
    昨天xx:xx
    :param created_at: 待转换的时间
    :return: datetime.date对象  微博发布日期
    """
    if '刚刚' in created_at:
        return datetime.now()
    elif '分钟' in created_at:
        minute = created_at[:created_at.find('分钟')]
        minute = timedelta(minutes=int(minute))
        created_time = datetime.now() - minute
        return created_time.date()
    elif '小时' in created_at:
        hour = created_at[:created_at.find('小时')]
        hour = timedelta(hours=int(hour))
        created_time = datetime.now() - hour
        return created_time.date()
    elif '昨天' in created_at:
        created_time = datetime.now() - timedelta(days=1)
        return created_time.date()
    else:
        l = created_at.split('-')
        month = l[-2]
        day = l[-1]
        year = datetime.now().year if len(l) == 2 else l[-3]
        return datetime(int(year), int(month), int(day)).date()
