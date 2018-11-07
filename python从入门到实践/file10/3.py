class Student(object):
    pass

def set_age(age): # 定义一个函数作为实例方法
    print(age)

s=Student()
s.set_age=set_age
s.set_age(2)