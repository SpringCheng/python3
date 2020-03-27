"""
1、子类的方法和父类的方法重名，子类重写父类方法，会调用子类的方法
2、super()子类方法需要调用父类方法

@File: 9.super关键词.py
@date: 2020/3/28 0:09 
@author：Spring
"""

from c3 import Human


class Student1(Human):
    # sum = 0
    #
    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self,name, age)
        super(Student1, self).__init__(name, age)
        # self.__score = 0
        # self.__class__ += 1
        # print(self.__dict__)

    def do_homework(self):
        super(Student1, self).get_name()
        print('you have to do homework')


studen1 = Student1('实验中学', '晨晨', 20)
print(studen1.name)
print(studen1.sum)
print(Student1.sum)
studen1.do_homework()
