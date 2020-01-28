# 对象拷贝

"""
1 直接拷贝内存地址值,没有创建新的对象,修改一个对象的属性,另外一个变量同时改变 浅拷贝      直接复制
    a = [1,2,3]
    b = a
2 拷贝的时候直接新创建一个对象,修改原来的一个对象的属性,不会影响另外一个变量的值, 深拷贝  分片
    a = [1,2,3]
    b =a[:]
a = [1,[2]]
b = a[:]
print(a)
print(b)
print("="*50)
b[0] = 100
b[1][0] =1000
print(a)
print(b)

对于深拷贝和浅拷贝,在python中的copy模块中有两个方法copy deepcopy
"""
# 导入拷贝的模块
import copy
a = [1,[2]]
# 浅拷贝 和分片操作一样
b = copy.copy(a)
# b[1][0] = 100 
print("浅拷贝",id(a[1]),id(b[1]))
c = copy.deepcopy(a)
c[1][0] = 100 
print("深拷贝",id(a[1]),id(c[1]))
print(a)
print(c)










