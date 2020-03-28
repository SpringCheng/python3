"""
# 对修改是封闭的，对扩展是开放的
这种方案的缺点：
@date: 2020/3/28 16:18 
@author：Spring
"""

import time


def f1():
    print('This is a function1')


def f2():
    print('This is a function2')


# func参数接受函数作为参数
def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)

