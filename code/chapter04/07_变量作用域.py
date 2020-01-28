# 全局变量
# 内置模块
"""
import builtins
print("内置模块:",dir(builtins))
b = 100
# 函数的嵌套定义
def fun_a(x,y):
    # 形式参数x,y 也是属于本地变量
    # 本地变量
    a = 100
    print("fun_a中访问:",sum)
    def fun_b():
        # a对于函数b来说是非本地变量
        c = 100
        print("访问本地变量:", b)
    fun_b()

    
fun_a()
#fun_b()
访问规则: ① 现在本地作用域 > ② 全局作用域(global) > ③ 内置作用域> ④ 报错 没有定义
"""

a = 100
def fun_a():
    # 在函数中修改全局变量 global
    # 声明变量a 为全局变量,如果外面没有,则会创建全局变量
    # global a
    # 本地变量
    a = 200
    def fun_b():
        # global a
        # 声明为非本地变量 需要注意的是外面的函数必须存在变量a
        nonlocal a
        a = 300
        print("函数fun_c中的值",a)
    fun_b()
    print("函数fun_a中的值",a)
fun_a()
print("全局中fun_a的值",a)

