from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session


class API(object):
    """
    自定义orm框架api接口
    """

    def __init__(self, engine):
        # 创建与数据库的会话session class， 这里返回给session的是个class，不是实列
        session_factory = sessionmaker(bind=engine)
        Session = scoped_session(session_factory)
        self.session = Session()

    def addone(self, obj, data):
        '''添加单条数据'''
        emp = obj(**data)
        try:
            # 添加数据
            self.session.add(emp)
            # 添加修改
            self.session.commit()
            # 返回结果
            self.session.close()
            return True, 'ok'
        except Exception as e:
            # 添加失败后回滚数据
            self.session.rollback()
            self.session.close()
            return False, e

    def addall(self, data):
        '''添加多条数据， data为多个对象的集合'''
        try:
            self.session.add(data)
            self.session.commit()
            self.session.close()
            return True, 'ok'
        except Exception as e:
            self.session.rollback()
            self.session.close
            return False, e

    def delete(self, obj, kwargs):
        '''删除指定数据'''
        emp = obj()
        # 判断传入的删除条件是否正确
        if kwargs is not None:
            for lib in kwargs.keys():
                # 如果emp中存在此属性就返回None，不存在就返回notexists
                res = getattr(emp, lib, 'notexists')
                if res == 'notexists':
                    self.session.close()
                    return False, '{0} is not defined'.format(lib)
        else:
            self.session.close()
            return False, '请指定删除条件, 如果要删除全部内容请使用deall()函数'
        # 查询判断要删除的值是否存在, 如果不存在会返回None
        res = self.session.query(obj).filter_by(**kwargs).all()
        if res:
            try:
                # 删除数据
                for re in res:
                    self.session.delete(re)
                    self.session.commit()
                self.session.close()
                return True, 'ok'
            except Exception as e:
                self.session.rollback()
                self.session.close()
                return False, e
        else:
            self.session.close()
            return False, 'notexists'

    def deleteall(self, obj):
        '''删除表种所有数据'''
        res = self.session.query(obj).all()
        if res:
            try:
                for re in res:
                    self.session.delete(re)
                    self.session.commit()
                self.session.close()
                return True, 'ok'
            except Exception as e:
                self.session.rollback()
                self.session.close()
                return False, e
        else:
            self.session.close()
            return False, 'table is not content'

    def change(self, obj, contents, kwargs):
        '''修改数据, contents是修改的列和修改后值的字典，kwargs是条件字典'''
        emp = obj()
        # 对传递进来的不定长参数进行判断
        if kwargs is not None:
            # 循环字典的键，即是表的属性，判断是否存在表中
            for lib in kwargs.keys():
                # 如果emp中存在此属性就返回None，不存在就返回notexists
                resu = getattr(emp, lib, 'notexists')
                if resu == 'notexists':
                    self.session.close()
                    return False, '{0} is not defind'.format(lib)
        else:
            self.session.close()
            return False, '请指定修改条件, 不允许一次修改全部内容'
        # 对更改数据的查询和更改进行异常判断
        try:
            res = self.session.query(obj).filter_by(**kwargs).all()
            for re in res:
                for content in contents:
                    # 更新对象属性内容
                    setattr(re, content, contents[content])
            self.session.commit()
            self.session.close()
            return True, 'ok'
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return False, e

    def query(self, obj, kwargs=None, nuique=False):
        '''查询指定对象， 返回列表包含的对象字典，可能是单个或多个'''
        emp = obj()
        res = None
        # 对传递进来的不定长参数进行判断
        if kwargs is not None:
            # 循环字典的键，即是表的属性，判断是否存在表中
            for lib in kwargs.keys():
                # 如果emp中存在此属性就返回None，不存在就返回notexists
                resu = getattr(emp, lib, 'notexists')
                if resu == 'notexists':
                    return None  # 查询失败就返回None
            # 查询指定内容
            if nuique:  # 如果指定了唯一参数就只返回一条数据
                res = self.session.query(obj).filter_by(**kwargs).first()
            else:
                res = self.session.query(obj).filter_by(**kwargs).all()
        else:
            # 没有指定参数就默认查询所有内容
            res = self.session.query(obj).all()
        self.session.close()
        return res

    def fuzzy_query(self, obj, kwargs, nuique=False):
        '''模糊查询'''
        res = None
        if nuique:
            res = self.session.query(obj).filter(*kwargs).first()
        else:
            res = self.session.query(obj).filter(*kwargs).all()
        self.session.close()
        return res
