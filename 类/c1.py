"""

@date: 2020/3/27 10:15 
@author：Spring
"""


class Student():
    name = 'cheng'
    age = 23

    def print_file(self):
        # 类中的函数不能直接访问类变量
        # 需要通过类.变量或者实例.变量访问

        # print('name:' + name)
        # print('age:' + str(age))

        # 正确写法(内部访问类中过的变量)
        print('name:' + self.name)
        print('age:' + str(self.age))
    # 类只负责调用，不负责调用
    # 运行类，调用类，要放在类的外部调用，c2

    # print_file()


student = Student()
student.print_file()
# 外部访问（类.变量）
print(Student.name)
print(student.name)
