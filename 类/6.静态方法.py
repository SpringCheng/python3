"""
1、对象和类都可以调用静态方法
2、静态方法可以访问类变量
3、静态方法是和当前类无关的方法，它只是
    一个保存到当前类中的函数，一般都是工具方法，和当前类无关

@File: 6.静态方法.py
@date: 2020/3/27 20:10 
@author：Spring
"""


class Student():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def add(x, y):
        result = x + y
        print('Total is:' + str(result))
        print(Student.sum)
        # print(self.name)

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
        # print(self.name)


Student.add(2, 3)

student1 = Student('xiaomi', 23)
student1.add(3, 5)
