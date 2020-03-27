"""
1、类：它将数据以及这些数据上的操作封装在了一起
2、构造函数
3、区别类变量和实例变量


@date: 2020/3/27 10:44 
@author：Spring
"""


class Student():
    """
    类中变量是否有意义：
        类应该是抽象，不应该是具体的，故name，age应该是定成实例变量，而不是
        类变量
    """
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


# class Printer():
#     def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))

student1 = Student('cheng', 12)
student2 = Student('chun', 21)

# 打印实例变量
print(student1.name)
print(student2.name)
# 打印类变量
print(Student.name)

# 对象的id是不同的
# student2 = Student()
# student3 = Student()

# print(id(student1))
# print(id(student2))
# print(id(student3))
