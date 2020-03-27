"""
1、类变量和实例变量的查询顺序
2、查找变量时候会先去实例变量里查找，如果实例变量里没有会向上去类变量里查找，
   若类里没有查找到，会去父类里查找
  （在模块下的函数是在函数局部作用域下查找，若没有则不会向上去模块下的全局变量查找）

@date: 2020/3/27 17:48 
@author：Spring
"""


class Student():
    name = 'aaa'
    age = 11

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)
    print(name)


student1 = Student()
print(student1.name)

# student1.__dict__保存着所有相关变量
# print(student1.__dict__)
# print(Student.__dict__)
