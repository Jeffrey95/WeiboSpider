# 数据库连接
DB_URL = 'mysql+pymysql://root:Mypasswd110~@localhost:3306/weibotest?charset=utf8mb4'
WEIBO_API_ROOT = 'https://m.weibo.cn/'
STATUS_DETAIL_URL = WEIBO_API_ROOT + 'statuses/extend?id={id}'
# 全部微博列表
WEIBO_LIST_URL = WEIBO_API_ROOT \
                 + 'api/container/getIndex?containerid=230413{id}_-_WEIBO_SECOND_PROFILE_WEIBO&page={page_num}'

# 原创微博列表
ORI_WEIBO_LIST_URL = WEIBO_API_ROOT \
                     + 'api/container/getIndex?containerid=230413{id}_-_WEIBO_SECOND_PROFILE_WEIBO_ORI&page={page_num}'

# 用户uid
UID_URL = 'http://open.weibo.com/widget/ajax_getuidnick.php'
# 用户粉丝
FANS_NUM_URL = WEIBO_API_ROOT + 'api/container/getIndex?type=uid&value={id}'
