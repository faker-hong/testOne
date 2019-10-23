from sqlalchemy import create_engine, Column, VARCHAR, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/xhx?charset=utf8", echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'brief_introduction1'
    name = Column(VARCHAR(255),primary_key = True)
    brief = Column(Text(0))


if __name__ == '__main__':
    u = User()
    u.name = 'hc'
    u.brief = '9797'
    DBSession = sessionmaker(bind=engine)   # 创建会话工厂，参数的意思是绑定我们之前连接的数据库。
    session = DBSession()                   # 获得了通信工具
    session.add(u)                          # 添加数据
    session.commit()                        # 添加
    session.close()                         # 关闭通信
    # 查询
    # session.execute('select * from brief_introduction1')