"""
1、函数可以作为一个返回结果
2、函数可以赋值给变量
    函数外的变量赋值并不会改变环境变量，比如：a=10
3、闭包条件： 闭包=函数+环境变量+return函数
    1、一个外部函数将变量和函数包起来叫做闭包
        1.1 变量a=25必须是在外部函数里，也要在内部函数外(在内部函数里
            形成不了闭包的条件,比如a=20,此时python认为a是一个局部变量
            不会去引用外部环境变量a=25)
        1.2、内部函数必须引用外部的环境变量，即curve必须调用a=25
    2、必须将内部函数作为返回值返回 比如：return curve
    3、函数的嵌套
4、用处
    4.1 通过闭包可以实现从外部访问内部函数
    4.2 通过闭包可以创建一些只有当前函数可以访问的变量，可以将一些私有的数据藏到闭包


5、 函数补充
    1、当我们使用一个变量时，会优先在当前作用域中查找该变量，
        如果有则使用，如果没有则继续去上一级作用域中寻找，
        局部变量调用全局变量可以直接调用
    2、如果局部变量和全局变量都有相同的变量，会优先调用局部变量

@File: 3.什么是闭包.py
@date: 2020/3/28 11:20 
@author：Spring
"""


def curve_pre():
    a = 25

    def curve(x):
        # a=20
        return a * x * x

    return curve


a = 10
f = curve_pre()
# f(2)  # f()就是curve()函数
print(f(2))

print('__________________________________________')

# 非闭包
step = 12


def go(origin):
    # 将局部变量step变成全局变量step=12
    global step
    new_pos = step + origin
    return new_pos


print(go(2))
print(go(3))

print('----------------------------------------')


# 函数式编程
origin = 0


# 这里的pos传入相当于pos是一个闭包的环境变量，但是在go函数里pos = new_pos认为pos是一个局部变量
# 报：local variable 'pos' referenced before assignment错误

def factory(pos):
    # 将pos设为不是本地的局部变量
    def go(step):
        nonlocal pos  # 此时的pos是外部函数传进来的环境变量
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


tourist = factory(origin)
print(tourist(2))
