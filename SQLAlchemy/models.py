import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, schema, Boolean, Enum, DateTime, Text, ForeignKey, LargeBinary

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/xhx?charset=utf8")
Base = declarative_base()


class User(Base):
    '''用户信息管理'''
    __tablename__ = 'user'

    Id = Column(Integer, primary_key=True, autoincrement='auto')
    username = Column(String(32), nullable=False, comment='用户名')
    password = Column(String(64), nullable=False, comment='密码')
    email = Column(String(100), default=None, comment='邮箱')


# 创建表
Base.metadata.create_all(engine)
