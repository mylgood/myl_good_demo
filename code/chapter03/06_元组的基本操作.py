# 创建元组
t1 = (1,2,3)
print(len(t1))
print(t1)
# 类型查看type
print(type(t1))

t2 =(1,[1,2])
print(t2)
#  不可变 : 元组里面的数据不能修改,删除,添加 长度是固定的
# 操作方法
# print(t2[-1][1])
# 不可变数据
# t2[0] = 100
t2[-1][1] =1000
# 分片操作 返回一个新的元组
print("分片:",t1[1:])
t1 = t1[1:]
print("t1:",t1) 
print(t2)

