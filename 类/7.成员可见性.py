"""
1、内外调用方法
2、共有和私有

@File: 7.成员可见性.py
@date: 2020/3/27 22:49 
@author：Spring
"""





# 内外调用方法

class Student():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add1(self):
        print('This is a add1 methond')

    def add2(self):
        print('This is a add2 methond')
        # 在类的内部一个函数可以去调用另外的函数
        self.add1()

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

# 在类的外部调用类方法
student1.add2()


print('********************************************************************')


# 公有和私有


class Student1():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0
        print(self.__dict__)

    # 加__双下划线不可以被外部访问
    def __add(self, x, y):
        total = x * y
        print(total)

    def marking(self, score):
        if score < 0 or score > 100:
            return '输入错误，请重新输入'
        else:
            self.__score = score
            print(self.name + '同学本次考试分数为：' + str(self.__score))

        # 类内可以访问私有函数
        self.__add(2, 3)


student2 = Student1('xumei', 18)
result = student2.marking(1)
# __将方法设为了私有方法，外部无法访问
# student2.__add(1, 2)

# 所有对于类下面变量的更改，都不应该直接更改,应该通过方法修改，保护数据
# Student1.score = -1

# 私有变量__score,无法访问
# print(student2.__score)

# 这个-1赋值给__score了，故无法通过动态的方式（加__）来添加私有变量
student2.__score = -1
print(student2.__dict__)


