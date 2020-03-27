"""
1、

@File: 5.类方法.py
@date: 2020/3/27 20:10 
@author：Spring
"""


class Student():
    sum = 0

    # 构造函数（意义：初始化类的特征）
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name)
        print(Student.sum)
