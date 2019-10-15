import cx_Oracle
import pymysql
import pygrametl
from pygrametl.datasources import SQLSource
from pygrametl.tables import FactTable


# 维度Dimension
# from pygrametl.tables import Dimension
#
# conn = pymysql.Connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='123456',
#     db='xhx',
#     charset='utf8'
# )
# # user表已存在
# user = [
#     {'username': '777', 'password': '777', 'email': '777'},
#     {'username': '888', 'password': '888', 'email': '888'},
#     {'username': '999', 'password': '999', 'email': '999'}
# ]
# pyconn = pygrametl.ConnectionWrapper(connection=conn)
# productDimension = Dimension(
#     name='user',
#     key='id',
#     attributes=['username', 'password', 'email'],
#     lookupatts=['username']
# )
# for row in user:
#     productDimension.insert(row)
# pyconn.commit()
# pyconn.close()



# FactTable
# conn = cx_Oracle.connect('TEST/123@localhost/orcl')
# conn = pygrametl.ConnectionWrapper(connection=conn)
# factTable = FactTable(
#     name='TEST',
#     measures=['score'],
#     keyrefs=['student_id', 'teacher_id', 'course_id']
# )
#
# facts =[
#     {'student_id': 1, 'course_id': 1, 'teacher_id': 1, 'score': 1},
#     {'student_id': 2, 'course_id': 2, 'teacher_id': 1, 'score': 2},
#     {'student_id': 1, 'course_id': 3, 'teacher_id': 1, 'score': 3}
# ]
# for row in facts:
#     factTable.insert(row)
# conn.commit()
#
# # re = factTable.lookup({'student_id': 1, 'course_id': 1, 'teacher_id': 1})
#
# newFacts = [
#     {'student_id': 1, 'abc': 1, 'teacher_id': 1, 'score': 1},
#     {'student_id': 2, 'abc': 2, 'teacher_id': 1, 'score': 2},
#     {'student_id': 1, 'abc': 2, 'teacher_id': 1, 'score': 3}]
#
# for row in newFacts:
#     factTable.ensure(row, True, {'COURSE_ID': 'abc'})
# conn.commit()
# conn.close()


# Oracle数据库
# conn = cx_Oracle.connect('TEST/123@localhost/orcl')
# sql = 'select * from student'
# newnames = 'ID', 'name'
# resultsSource = SQLSource(connection=conn, query=sql, names=newnames)
# print(type(resultsSource))
#
# for row in resultsSource:
#     print(row)
#     print(row["name"])


# Mysql
# conn = pymysql.Connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='123456',
#     db='xhx',
#     charset='utf8'
# )
# sql = 'select * from user'
# newnames = 'id', 'username', 'password', 'email'
# resultsSource = SQLSource(connection=conn, query=sql, names=newnames)

# CSV文件
