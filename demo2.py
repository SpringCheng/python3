"""

@date: 2020/3/25 9:12 
@author：Spring
"""

# 不能是常量
# 代码块中有限制的语句
# counter = 1
# while counter <= 10:
#     counter += 1
#     print(counter)

# a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3, 4)]
# for x in a:
#     for y in x:
#         if y == 'banana':
#             break
#         print(y, end=' ')

for x in range(0, 10, 2):
    print(x)

a = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(0, len(a), 2):
    print(a[i], end=' ')

print(a[::2])
b = a[0:len(a):2]
print(b)
