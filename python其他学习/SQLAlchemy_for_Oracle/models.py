from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import cx_Oracle
import os

os.environ["NLS_LANG"] = "GERMAN_GERMANY.UTF8"
engine = create_engine('oracle+cx_oracle://TEST:123@orcl', echo=True)


# engine = create_engine('oracle://TEST:123@localhost:1521/Test', echo=True)
Base = declarative_base()


class Course(Base):
    '''课程表'''
    __tablename__ = 'course'

    ID = Column(Integer, primary_key=True, autoincrement=True, comment='课程编号')
    name = Column(String(20), nullable=True, comment='课程名')


class Student(Base):
    '''学生表'''
    __tablename__ = 'student'

    ID = Column(Integer, primary_key=True, autoincrement=True, comment='学生编号')
    name = Column(String(10), nullable=True, comment='学生名')


class Student_Course(Base):
    '''成绩表'''
    __tablename__ = 'student_course'
    ID = Column(Integer, primary_key=True, autoincrement=True, comment='成绩编号')
    student_id = Column(Integer, comment='学生编号')
    course_id = Column(Integer, comment='课程编号')
    teacher_id = Column(Integer, comment='老师编号')
    score = Column(Integer, comment='成绩分数')


class Teacher(Base):
    '''老师表'''
    __tablename__ = 'teacher'
    ID = Column(Integer, primary_key=True, autoincrement=True, comment='老师编号')
    name = Column(String(10), comment='老师姓名')


# 创建表
Base.metadata.create_all(engine)