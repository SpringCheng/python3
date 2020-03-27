"""

序列解包
@date: 2020/3/26 10:28 
@author：Spring
"""


# a = 100
# b = 200
# b, a = a, b
# print(a, b)


# def fn(a, b, c):
#     print(a, b, c)
#
#
# t = (10, 20, 30)
# fn(*t)


# def fn(a, b, c):
#     print(a, b, c)
#
#
# t = {'a': 1, 'b': 2, 'c': 'apple'}
# fn(**t)

def chide(xiaocai, zhushi, tianpin='黑森林可乐', *shaokao):
    print('一盘小菜：' + xiaocai)
    print('主食来啦：' + zhushi)
    print('一份甜品：' + tianpin)
    for i in shaokao:
        print('烧烤之一：' + i)


chide('炒豆苗', '馒头', '樱桃布丁', '羊肉串', '肉筋', '板筋', '烤韭菜')


a = 12


def egg():
    # global语句将变量quantity声明为全局变量
    global quantity
    print(a)
    quantity = 108


egg()
print(quantity)
