# 函数的嵌套调用
"""
def fun_a():
    print("执行函数a")
    
def fun_b():
    print("开始执行函数b")
    fun_a()
    print("完成函数b执行")
fun_b()
"""

# 
b = 100
# 函数的嵌套定义
def fun_a():
    print("外面的b的值是:",b)
    a = 100
    print("里面的a的值是:",a)
    print("开始执行函数a")
    def fun_b():
        print("执行函数b")
    fun_b()
    print("完成函数a执行")
    
fun_a()
#fun_b()
print("最后访问b",b)
print("全局访问 里面的a的值是:",a)
