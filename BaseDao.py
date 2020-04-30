# -*- encoding:utf-8 -*-

import pymysql
import Student as student

s = student.Student()

# 1.查询所有学生信息
def getAll():
    connect = pymysql.connect(host="192.168.43.21", user="user, passwd="1234", db="zs")
    cursor = connect.cursor()
    cursor.execute("select * from Student")
    data = cursor.fetchall()
    connect.close()
    return data


# 根据学生姓名查询学生信息
def getStudentBySname(s):
    connect = pymysql.connect(host="192.168.43.21", user="user", passwd="1234", db="zs")
    cursor = connect.cursor()
    sql = "select *  from Student where sname='%s'" % (s.getSname())
    cursor.execute(sql)
    data = cursor.fetchall()
    connect.close()
    return data


# 根据sid查询单个学生信息
def getStudentBySid(s):
    connect = pymysql.connect(host="192.168.43.21", user="user", passwd="1234", db="zs")
    cursor = connect.cursor()
    sql = "select *  from Student where sid=%d" % (s.getSid())
    cursor.execute(sql)
    data = cursor.fetchone()
    connect.close()
    return data


# 添加学生信息
def addStudent(s):
    connect = pymysql.connect(host="192.168.43.21", user="user", passwd="1234", db="zs")
    cursor = connect.cursor()
    sql = "insert into Student values(null,'%s','%s','%d')" % (s.getSname(), s.getSsex(), s.getSage())
    cursor.execute(sql)
    connect.commit()
    connect.close()


# 删除学生信息
def delStudent(s):
    connect = pymysql.connect(host="192.168.43.21", user="user", passwd="1234", db="zs")
    cursor = connect.cursor()
    sql = "delete from Student where sid=%d" % (s.getSid())
    cursor.execute(sql)
    connect.commit()
    connect.close()


# 修改学生信息
def updStudent(s):
    connect = pymysql.connect(host="192.168.43.21", user="user", passwd="1234", db="zs")
    cursor = connect.cursor()
    sql = "update Student set sname='%s',ssex='%s',sage=%d where sid=%d" % (
    s.getSname(), s.getSsex(), s.getSage(), s.getSid())
    cursor.execute(sql)
    connect.commit()
    connect.close()


# 根据查询条件查询学生信息
def selectStu(s):
    connect = pymysql.connect(host="192.168.43.21", user="user", passwd="1234", db="zs")
    cursor = connect.cursor()
    sql = "select * from Student where 1=1"
    if(s.getSid()!=""):
        sql=sql+" and sid=%d"%(s.getSid())
    if(s.getSname()!=""):
        sql=sql+" and sname like '%%%s%%'"%(s.getSname())
    if(s.getSsex()!=""):
        sql=sql+" and ssex='%s'"%(s.getSsex())
    if(s.getSage()!=""):
        sql=sql+" and sage=%d"%(s.getSage())
    cursor.execute(sql)
    data = cursor.fetchall()
    connect.close()
    return data


# 测试查询所有学生信息
# d=getAll()
# print(d)

# 测试查询单个学生信息
# stu = student.Student()
# stu.setSname("小明")
# sd = getStudentBySname(stu)
# print(sd)

# 测试添加学生信息
# s= student.Student()
# s.setSname("小明")
# s.setSsex("男")
# s.setSage(19)
# addStudent(s)

# 测试删除学生信息
# stu = student.Student()
# stu.setSid(9)
# delStudent(stu)

# 测试修改
# s= student.Student()
# s.setSid(15)
# s.setSname("小d")
# s.setSsex("男")
# s.setSage(19)
# updStudent(s)

# 测试根据查询条件查询学生信息
# stu = student.Student()
# stu.setSname("s")
# print(stu.getSname()!="")