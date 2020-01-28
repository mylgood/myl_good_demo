# 对象拷贝
""""""
list1 = [1,2,3]
# 赋值操作 内存地址是
list2 = list1
print("="*50)
print(list1)
print(list2)
# 修改list2里面的值
list2[0] = 100 #[100,2,3]
print("="*50)
print(list1)
print(list2)
print("内存比较")
print("list1",id(list1))
print("list2",id(list2))

"""
# 分片操作
list1 = [1,2,3]
list2 =list1[:] # 通过分片操作对象拷贝
print("="*50)
print(list1)
print(list2)
list2[0] = 100 
print("="*50)
print(list1)
print(list2)
print("内存比较")
print("list1",id(list1))
print("list2",id(list2))
"""


