# reduce(fn,序列) 用于做累计运算
# fn: 函数, 有两个参数, 返回一个值 
# 返回一个需要累计的值
# 需求
"""
list_a = [2,4,6,8,10]
ret = 1
for item in list_a:
    ret *= item    
print(ret)
"""
"""
from functools import reduce
list_a = [2,4,6,8,10]
ret = reduce(lambda x,y: x*y,list_a)
print(ret)
"""
# 需求: 给定一个list集合, 把其中所有的大于80的数据都找出来
list_a = [112,124,46,58,110]
list_b = []
"""
for item in list_a:
    if item > 80:
        list_b.append(item)
print("list_b:",list_b)
"""
# filter(fn,序列)用来过滤
#fn 接受一个参数,返回一个布尔值
ret = filter(lambda x: x>80,list_a)
print(list(ret))
# map reduce filter sorted

