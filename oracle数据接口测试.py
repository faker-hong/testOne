import cx_Oracle

class Api(object):
    # 连接数据库
    def __init__(self):
        self.conn = cx_Oracle.connect('TEST/123@localhost/orcl')
        self.cursor = self.conn.cursor()

    # 关闭连接
    def close_all(self):
        self.cursor.close()
        self.conn.close()

    # 全查
    def query_all(self):
        self.cursor.execute('select id, name, phone, address from users')
        res = self.cursor.fetchall()
        self.close_all()
        return res

    # 按id查询
    def query_by_name(self, id):
        self.cursor.execute('select id, name, phone, address from users where id={}'.format(id))
        res = self.cursor.fetchall()
        self.close_all()
        return res

    # 新增记录
    def insert(self, data):
        sql = 'insert into users values(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(*data)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.close_all()
            print('新增成功')
            return
        except Exception as e:
            # 添加后失败回滚
            self.conn.rollback()
            self.close_all()
            print('新增失败')
            return

    # 删除记录
    def delete(self, id):
        sql = 'delete from users where id={}'.format(id)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.close_all()
            print('删除成功')
            return
        except Exception as e:
            self.conn.rollback()
            self.close_all()
            print('删除失败')
            return

    # 修改记录
    def update(self, id, phone):
        sql = 'update users set phone={} where id={}'.format(phone, id)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.close_all()
            print('修改成功')
            return
        except Exception as e:
            self.conn.rollback()
            self.close_all()
            print('修改失败')
            return


if __name__ == '__main__':
    a = Api()
    # re = a.query_by_name('1')
    # re = a.query_all()
    data = ['3', '测试', '男', '123456', '上海']
    re = a.insert(data)
    # print(re)
    # a.delete('3')
    # a.update('1', '666666')