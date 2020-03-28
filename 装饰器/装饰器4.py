"""
被装饰的函数有多个参数的情况
加入* args
@date: 2020/3/28 16:18 
@author：Spring
"""

import time


def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)

    return wrapper


# f1有参数的情况
@decorator
def f1(func_name,func_age):
    print('This is a function ' + func_name+str(func_age))


f1('cccc',23)
