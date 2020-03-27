"""
self：
    谁调用self，self就指代了谁，self本身代表一个实例，一个对象
    self和其他的语言的this一样，self只和对象有关
实例方法：
    1、实例方法必须放入一个self
    2、调用实例方法时，不需要对self传参
    3、实例调用的方法
@date: 2020/3/27 18:19 
@author：Spring
"""


class Student():
    name = 'spring'
    age = 0

    # 构造函数（初始化函数）
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("这是构造函数")
        # return 'student'

    def do_homework(self):
        print('homework')


class Printer():
    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

student1 = Student('cheng', 12)
student2 = Student('chun', 21)