"""
reduce(function, sequence, initial=None)

连续计算，连续调用lambda

@date: 2020/3/28 14:28 
@author：Spring
"""
from functools import reduce

list_x = [1, 2, 3, 4, 5]
list_y = [23, 4, 5, 66,3]

r=reduce(lambda x, y: x + y, list_x)
print(r)  # 15


"""
x=1  y=2  x+y=3
x=3  y=3  x+y=6
x=6  y=4  x+y=10
x=10 y=5  x+y=15 
((((1+2)+3)+4)+5)
"""