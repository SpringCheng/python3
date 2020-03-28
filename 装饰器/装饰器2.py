"""
装饰器特点：
1、返回函数，return wrapper
2、必须传入一个函数  func
@date: 2020/3/28 16:18 
@author：Spring
"""

import time


def decorator(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


def f1():
    print('This is a function')


f = decorator(f1)
f()
