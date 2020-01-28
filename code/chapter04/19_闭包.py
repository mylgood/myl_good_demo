#需求: 提供一个函数,用于生产一个自动增长的数字 1,2,3,4,5
# 闭包:
# 1: 函数A中定义函数B 
# 2: 函数A 返回函数B
# 3: 函数B 中访问了函数A中的变量


def get_id():
    num = 0
    def gen_id():
        nonlocal num
        num += 1
        return num
    return gen_id

# num = 100
callback = get_id()
print(callback())
print(callback())
num = 0
print(callback())
print(callback())