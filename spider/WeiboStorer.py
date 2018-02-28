from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.urls import DB_URL
import logging

engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(engine)


class WeiboStorer:
    def __init__(self):
        self.session = Session()

    def store_weibo_to_db(self, weibo_list):
        """
        将微博存到数据库
        :param weibo_list: Class为Weibo的列表，Weibo字段的定义见db.TableDef
        :return: # todo 存储成功返回True,失败返回False
        """
        if not weibo_list:
            return
        self.session.add_all(weibo_list)
        try:
            self.session.commit()
        except Exception as e:
            logging.warning(e)
            self.session.rollback()