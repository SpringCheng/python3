"""
1、添加__使得类内部的变量和方法外部无法访问
    1.1、外部使用self__name=name实际上是将name赋值给了__name
2、设置getter和setter方法

@File: 7.2封装.py
@date: 2020/3/28 0:56 
@author：Spring
"""


class Dog:
    def __init__(self, name):
        print('aaa')
        self.__name = name
        print(self.__dict__)

    # getter 方法的装饰器
    # property装饰器将一个get方法转换为对象的属性
    # 添加property装饰器后，我们可以像调用属性来调用get方法
    # 使用property装饰器的方法，必须和属性名相同
    @property
    def name(self):
        print('这是getter方法')
        return self.__name

    # setter方法的装饰器
    # 格式：  @属性名.setter
    @name.setter
    def name(self, name):
        print('setter方法')
        self.__name = name


d1 = Dog('旺财')

# 这里能改变私有变量的原因是将’哈哈‘赋值给了__name变量
# d1.__name = 'haha'
# print(d1.__name)

# 设置了getter方法后
print(d1.name)
print('*********************')
# 因为设置了getter方法装饰，故d1.name='白骨精'不可以设置
d1.name = '白骨精'
# 若需要设置变量值，需要设置个setter方法

d1.name = '小黑'
print(d1.name)
