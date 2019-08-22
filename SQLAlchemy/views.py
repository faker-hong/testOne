from SQLAlchemy.models import engine, User
from SQLAlchemy.databaseApi import API


# 初始化数据库操作引擎
db = API(engine)

# 添加数据
# data = {
#     'username': '97',
#     'password': '123456',
#     'email':  'hongcheng97@163.com'
# }
#
# res, text = db.addone(User, data)

# 完全匹配查询
# res = db.query(User)
# res = db.query(User, {'username': '9797'}) # 指定姓名
# res = db.query(User, {'username': 'zhangsan'}, True) # 指定返回单条数据
# 不完全匹配查询
# res = db.fuzzy_query(User, {User.username.like('9%')}) # 查询所有以zhang开头的
# res = db.fuzzy_query(User, {User.name.like('zhang%'), User.eamil != None}) # 添加条件，性zhang并且邮箱不为空的

# 删除数据
# res, e = db.delete(User, {'username' : '97'})
# res, e = db.deleteall(User) # 这个方法删除表中的所有数据，慎用。

# 修改数据
# 第一个参数是修改的表，第二个参数是修改的字段和修改后的值，第三个参数是修改的条件
# res, e = db.change(User, {'email': 'zhang_san@163.com'}, {'username' : '9797'})
