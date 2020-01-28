"""
在程序运行的过程中,把创建的对象而且已经是没有用的对象自动回收, 这个过程称之为垃圾回收
"""
a = "python"
print(a)
# 把a中的对象数据赋值给变量b
# a,b两个变量共享引用数据"python"
b = a
print(id(a))
print(id(b))
a = "wolfcode"
print(a)
print(id(a))
print(id(b))
b = "java"
