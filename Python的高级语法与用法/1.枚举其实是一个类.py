"""
1、枚举关注的是名字，类.变量 返回的是类.变量
    1.1、继承自Enum
2、枚举的特点
    2.1、访问枚举类中的某一项，直接使用类名访问加上要访问的项即可，比如 color.YELLOW
    2.2、枚举的意义在于标签而不是后面的值
    2.3、枚举和普通类的区别
        2.3.1、字典和变量容易被改变，枚举不能被改变
        2.3.2、导入Enum之后，一个枚举类中的Key和Value，Key不能相同，Value可以相，但是Value相同的各项Key都会当做别名
    2.4、获取枚举值
        VIP.GREEN.value
    2.4、获取枚举名字
        VIP.GREEN.name
    2.5、枚举可以遍历
        for v in VIP:
            print(v)
    2.6、 枚举之间的比较
        1、枚举类型不能比较
            print(VIP.GREEN>VIP.RED)
        2、能做等值比较
            print(VIP.GREEN==VIP.RED)
        3、能做身份的比较
            print(VIP.GREEN IS VIP.RED)
    2.7、枚举的注意事项
        1、如果两个枚举类型的数值相同，第二个是第一个的别名
        from enum import Enum
        class Vip(Enum):
          YELLOW=1
          YELLOW_ALIES=1

        2、如果要枚举类中的Value只能是整型数字，那么，可以导入IntEnum，然后继承IntEnum即可，
            注意，此时，如果value为字符串的数字，也不会报错
@File: 1.枚举其实是一个类.py
@date: 2020/3/28 10:00 
@author：Spring
"""

from enum import Enum


class Color:
    YELLOW = 1
    YELLOW = 3  # 注意这里又将YELLOW赋值为3，会覆盖前面的1
    RED = 2
    GREEN = 3
    PINK = 4


# 访问枚举项
print(Color.YELLOW)  # 3

# 但是可以在外部修改定义的枚举项的值，这是不应该发生的
Color.YELLOW = 99
print(Color.YELLOW)  # 99

print("------------------------------------------------------------------")


# 继承枚举类
class color(Enum):
    YELLOW = 1
    BEOWN = 1
    # 注意BROWN的值和YELLOW的值相同，这是允许的，此时的BROWN相当于YELLOW的别名
    RED = 2
    GREEN = 3
    PINK = 4


class color2(Enum):
    YELLOW = 1
    RED = 2
    GREEN = 3
    PINK = 4


print(color.YELLOW)  # color.YELLOW
print(type(color.YELLOW))  # <enum 'color'>

print(color.YELLOW.value)  # 1
print(type(color.YELLOW.value))  # <class 'int'>

print(color.YELLOW == 1)  # False
print(color.YELLOW.value == 1)  # True
print(color.YELLOW == color.YELLOW)  # True
print(color.YELLOW == color2.YELLOW)  # False
print(color.YELLOW is color2.YELLOW)  # False
print(color.YELLOW is color.YELLOW)  # True

print(color(1))  # color.YELLOW
print(type(color(1)))  # <enum 'color'>


# 枚举类里面定义的Key = Value，在类外部不能修改Value值，也就是说下面这个做法是错误的
color.YELLOW = 2  # Wrong, can't reassign member
