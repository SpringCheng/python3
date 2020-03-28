"""
# 函数时编程
1、闭包
2、map()函数
    map(func, *iterables)
3、lambda和三元表达式使用
@date: 2020/3/28 14:02 
@author：Spring
"""

l = [1, 2, 3, 4, 5]
a = map(lambda i: i * i, l)

print(list(a))

list_x = [1, 2, 3, 4, 5]
list_y = [23, 4, 5, 66]  # 若列表里面元素不相等，以最短的为基准

b = map(lambda x, y: x + y, list_x, list_y)
print(list(b))