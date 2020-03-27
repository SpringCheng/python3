"""

@File: 8.继承.py
@date: 2020/3/27 23:36 
@author：Spring
"""

from c3 import Human


class Student1(Human):
    # sum = 0
    #
    # def __init__(self, school):
    #     self.school = school
        # self.__score = 0
        # self.__class__ += 1
        # print(self.__dict__)

    def do_homework(self):
        print('you have to do homework')


studen1 = Student1('晨晨', 20)
print(studen1.name)
print(studen1.sum)
print(Student1.sum)
studen1.get_name()
