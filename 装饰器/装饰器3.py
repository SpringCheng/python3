"""
语法糖

@date: 2020/3/28 16:18 
@author：Spring
"""

import time


def decorator(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


@decorator
def f1():
    print('This is a function')


f1()
