from SQLAlchemy_for_Oracle.models import engine, Course, Teacher, Student_Course
from SQLAlchemy_for_Oracle.databaseApi import Api
from SQLAlchemy_for_Oracle.models import Student

# 初始化操作引擎
db = Api(engine)

# 添加
# data = {
#     'ID': 2,
#     'student_id': '10001',
#     'course_id': '30002',
#     'teacher_id': '20002',
#     'score': 59,
# }
# re = db.addone(Student_Course, data)

# 修改
# contents = {
#     'name': '97'
# }
# data = {
#     'ID': 10086
# }
# re = db.update(Student, contents, data)

# 删除
# kwargs = {
#     'ID': '10086'
# }
# re = db.delete(Student, kwargs)

# 查询
# kwargs = {
#     'name': '9797'
# }
# res = db.query_by_options(Student, kwargs)

# 查询平均成绩大于60分的同学的学号和平均成绩
# res = db.avg_higher_sixty()
# print(res)

# 查询所有同学的学号,姓名、选课数、总成绩
# res = db.all_student_info()

# 学过a和b课程的同学的学号、姓名
# courses = ['30001', '30002']
# res = db.study_courses(courses)
# print(res)