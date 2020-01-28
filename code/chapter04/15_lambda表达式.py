# 用于计算两个数的和
'''
def sum(x,y):
    """ 用于计算两个数的和"""
    return x + y
sum2 = lambda x,y:x+y
print(sum(1,2))
print(sum2(1,9))
print(sum2)
# 通过lambda表达式简化代码

# lambda 可以所谓一个函数的参数

def go_home(callback):
    print("开始执行")
    callback();
    print("完成执行")
    
# fn = lambda : print("lmbda函数")
go_home(lambda : print("lmbda函数"))
'''
'''
def max(x,y):
    "返回x,y中的最大值"
    """
    if x >= y:
        return x
    else:
        return y
    """
    # 三元运算符
    return x if x >= y else y
# lambda 表达式用于逻辑比较简单,
max2  = lambda x,y:x if x >= y else y
print(max(10,4))
print(max2(99,78))
'''
def max(x,y,z):
    """返回x,y,z中的最大声"""
    """
    return x if x>=y and x >= z else  y if y>=x and y>=z else z

    """
    print(123)
    print(456)
    if x>=y and x >= z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z
    
# 在不够清晰的时候,不建议使用lambda表达式
max2 = lambda x,y,z:x if x>=y and x >= z else  y if y>=x and y>=z else z
print(max(1,13,5))
print(max2(1,13,5))
print("*"*50)

# 在表达式中执行多个语句 需要使用逻辑运算符or 或者 and 
max3 = lambda x,y,z:print(123) or print(456) or (x if x>=y and x >= z else  y if y>=x and y>=z else z)
print(max3(1,13,5))
        