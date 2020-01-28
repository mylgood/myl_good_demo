
def fun_a(x,y):
    #x[0] = 9
    print("fun_a:",x,y)
"""
a = [100]
b = [200]
fun_a(a,b)
print("全局变量",a,b)
"""
# 位置参数传递
fun_a(1,2)
# 关键字参数 在函数调用的时候,使用name = value 
fun_a(y=9, x=10)

def fun_b(x, y, z):
    print("fun_b",x,y,z)
    
fun_b(1,2,3)
# 对于关键字参数和位置参数可以结合使用
# 位置参数必须在关键字参数前面
fun_b(10,z=200,y=300)
# 错误
# fun_b(z=200,y=300,2000)

def fun_c(x,y=10,z=20):
    print("fun_c",x,y,z)
# 在有默认参数的时候,实际参数可以和形式参数不相等,没有传递的参数使用默认值
fun_c(10)
fun_c(10,2) 
fun_c(1,2,3)   
# 需求: 如果y使用默认值, 其他参数x 4 z 6
fun_c(4,z=6)  

print(123,end="\t")
print(456,end="\t")
print(help(print))


