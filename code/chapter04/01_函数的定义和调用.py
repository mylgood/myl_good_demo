"""
函数的定义:
    def 函数名([参数1,参数2,...,参数n]):
        函数体
        [return 值]
"""
# 定义函数
# 函数名称 就是一个变量
def talk():
    print("你好,兄弟")

# 函数调用
talk()
talk()
print(type(talk))
print(len([1,2,3]))
# 内置模块
import builtins
# dir 查看模块中有哪些方法和函数
print(dir(builtins))
    
    

