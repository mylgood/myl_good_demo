"""
函数的定义:
    def 函数名([参数1,参数2,...,参数n]):
        函数体
        [return 值]
"""

def fn():
    print("执行函数")
    # 元组的装包功能
    return 100,200,300

# 定义一个ret变量接受fn(函数)的返回值
# 没有return 返回一个None ,如果有return 直接返回后面的值,如果返回的是多个值,会包装为一个元组返回
x,y,z = fn();
print("返回结果",x,y,z )
#print(type(ret))
print("程序结束")

    

