# 创建一个range
# 创建一个[0,10)的一个整数的数据
r1 = range(10)
print(r1)
print(len(r1))
print(type(r1))
# 有序序列
print(r1[0])
print(r1[-1])
# for item in r1:
#    print(item)
list1 = list(r1)
print(list1)
print(100 in r1)

# 生成[5,10)的range数据
r2 =range(10,4,-2)
print(list(r2))