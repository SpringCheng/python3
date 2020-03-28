"""


@date: 2020/3/28 12:28 
@author：Spring
"""

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