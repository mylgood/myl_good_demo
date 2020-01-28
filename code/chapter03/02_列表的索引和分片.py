# 可变对象
list1 = [1,2,3]
# 索引操作
print(list1[0])
print(list1[-1])
list1[0] = 100
# 删除
del list1[2]
# 分片操作
list2 = list1[:]
# 插入 线删除 [0,2)的元素,然后在开始索引0位置插入新的元素
list1[0:2] = [10,20,300]
# 模拟删除
list1[0:2] = [] # [300]
# 添加操作
list1[0:0] =[100,200,300] # [100,200,300,300]

print("list2:",list2)
print("list1",list1)

# for 遍历序列
for item in list1:
    print(item)