"""

@File: c3.py
@date: 2020/3/27 23:43 
@author：Spring
"""


class Human():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)
