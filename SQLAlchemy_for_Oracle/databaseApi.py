from sqlalchemy.orm import sessionmaker, scoped_session


class Api(object):
    """
        自定义orm框架api接口
    """
    def __init__(self, engine):
        # 创建与数据库的会话session class， 这里返回给session的是个class，不是实列
        session_factory = sessionmaker(bind=engine)
        Session = scoped_session(session_factory)   # scoped_session类似与单例，不能同时对一个session进行操作
        self.session = Session()

    def addone(self, obj, data):
        '''添加单条数据'''
        emp = obj(**data)
        try:
            # 添加数据
            self.session.add(emp)
            # 提交
            self.session.commit()
            # 关闭连接
            self.session.close()
            return True, 'OK'
        except Exception as e:
            # 失败后回滚
            self.session.rollback()
            self.session.close()
            return False, e

    def addall(self, data):
        '''添加多条数据'''
        try:
            self.session.add(data)
            self.session.commit()
            self.session.close()
            return True, 'OK'
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return False, e

    def delete(self, obj, kwargs):
        '''删除一条数据'''
        emp = obj()
        if kwargs is not None:
            # 判断传入的key是否存在类中
            for lib in kwargs.keys():
                res = getattr(emp, lib, 'notexists')
                if res == 'notexists':
                    self.session.close()
                    return False, '{}is not exists'.format(lib)
        else:
            self.session.close()
            return False, '请指定删除条件'
        res = self.session.query(obj).filter_by(**kwargs).all()
        if res:
            for re in res:
                self.session.delete(re)
                self.session.commit()
            self.session.close()
            return True, 'OK'
        else:
            self.session.close()
            return False, 'notexists'

    def update(self, obj, contents, kwargs):
        emp = obj()
        if kwargs is not None:
            for lib in kwargs.keys():
                res = getattr(emp, lib, 'notesists')
                if res == 'notesists':
                    self.session.close()
                    return False, '{} is not exists'.format(lib)
        else:
            self.session.close()
            return False, '请指定修改条件'

        try:
            res = self.session.query(obj).filter_by(**kwargs).all()
            for re in res:
                for content in contents:
                    setattr(re, content, contents[content])
            self.session.commit()
            self.session.close()
            return True, 'OK'
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return False, e

    def query_by_options(self, obj, kwargs):
        emp = obj()
        if kwargs is not None:
            for lib in kwargs.keys():
                res = getattr(emp, lib, 'notexists')
                if res == 'notexists':
                    self.session.close()
                    return False, '{} not exists'.format(lib)
        else:
            res = self.session.query(obj).all()
            self.session.close()
            return res
        try:
            res = self.session.query(obj).filter_by(**kwargs).all()
            self.session.close()
            return res, 'OK'
        except Exception as e:
            self.session.close()
            return False, e

    # 查询平均成绩大于60分的同学的学号和平均成绩
    def avg_higher_sixty(self):
        try:
            sql = 'SELECT s.id, avg(sc.score) ' \
                  'from student s, STUDENT_COURSE sc ' \
                  'where s.id = SC.STUDENT_ID ' \
                  'group by s.id'
            res = self.session.execute(sql).fetchall()
            self.session.close()
            return res
        except Exception as e:
            self.session.close()
            return False, e

    # 查询所有同学的学号,姓名、选课数、总成绩
    def all_student_info(self):
        try:
            sql = 'select s.id, s.name, sc.cu 选课数, sc.su 总分 ' \
                  'from student s, (select student_id, count(1) cu, sum(score) su from STUDENT_COURSE GROUP BY student_id) sc ' \
                  'where s.id = sc.student_id'
            res = self.session.execute(sql).fetchall()
            self.session.close()
            return res
        except Exception as e:
            self.session.close()
            return False, e

    # 学过a和b课程的同学的学号、姓名
    def study_courses(self, courses):
        try:
            sql = "select s.id, s.name " \
                  "from student s,STUDENT_COURSE sc " \
                  "where s.id = sc.student_id and sc.course_id = '{}' and " \
                  "EXISTS( select 1 from STUDENT_COURSE a where COURSE_id = '{}' " \
                  "and a.student_id = sc.student_id) GROUP BY s.id, s.name".format(*courses)
            res = self.session.execute(sql).fetchall()
            self.session.close()
            return res
        except Exception as e:
            self.session.close()
            return False, e