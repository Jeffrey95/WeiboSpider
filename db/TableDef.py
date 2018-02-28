from sqlalchemy import Column, String, Date, Boolean, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from config.urls import DB_URL

Base = declarative_base()
engine = create_engine(DB_URL, echo=True)


class Weibo(Base):
    __tablename__ = 'weibo'
    weibo_id = Column(String(30), primary_key=True, comment='微博id')
    bid = Column(String(20), comment='微博id')
    nickname = Column(String(20), comment='用户昵称')
    created_at = Column(Date, comment='微博发布时间')
    is_retweet = Column(Boolean, comment='是否转发')
    title = Column(String(500), comment='微博标题')
    text = Column(String(10000), comment='微博文本')
    source = Column(String(20), comment='微博来源')
    page_exist = Column(Boolean, comment='是否有外链')
    pic_exist = Column(Boolean, comment='是否有图片')
    has_cleaned = Column(Boolean, comment='数据是否已经清洗')
    is_long_text = Column(Boolean, comment='是否长微博')
    crawl_complete = Column(Boolean, comment='是否已获取微博全文')


class Uid(Base):
    __tablename__ = 'uid'
    uid = Column(String(20), primary_key=True, comment='用户id')
    nickname = Column(String(20), comment='用户昵称')
    fans = Column(Integer, comment='粉丝数')


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
