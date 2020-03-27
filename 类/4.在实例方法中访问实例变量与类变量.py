"""
1、函数外部和实例方法内部访问类变量都是
        类.变量
2、类方法访问类变量
        @classmethod
        def stu(cls):
            print(cls.sum)
3、类变量的修改
    方法一：通过类方法修改
        @classmethod
        def sss(cls):
            cls.sum = input('请输入任意字符')
    方法二：外部  类.变量修改
        Student.sum=input('请输入数字')
        print(Student.sum)
@date: 2020/3/27 18:57 
@author：Spring
"""


# 实例方法访问实例变量
#     self.name
# 实例方法内部访问类变量？
class Student():
    sum = 0

    # 构造函数（意义：初始化类的特征）
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 访问实例变量，两种方法都可以，最好加上self.name
        # print(name)
        print(self.name)

        # 实例方法内部不能直接访问类变量
        # print(sum)
        # 正确访问
        print(Student.sum)

    # 实例方法
    def do_homework():
        print("homewordk hvae done")

    # 类方法
    @classmethod
    def stu(cls):
        print(cls.sum)

    # 类变量的修改方法一
    @classmethod
    def sss(cls):
        cls.sum = input('请输入任意字符')


student1 = Student('beatufy', 19)
print(Student.sum)

# 修改类变量方法二
Student.sum=input('请输入数字')
print(Student.sum)