"""

"""
list1 = [1,2,3]
# 增加方法 在末尾添加一个元素 在原来的list1的基础上进行修改,返回值是None
ret = list1.append(50)
# 把列表当成一个元素插入
# list1.append(["a","b","c"])
# 如果需要合并两个元素
list1.extend(["a","b","c"])
# 插入 索引
list1.insert(0,100)
# 如果索引不在范围内,如果是正数,插入到末尾,如果是负数,插入在开始的位置
list1.insert(-1000,1000)
# 删除 根据值来删除元素,如果没有,直接报错ValueError
list1.remove(2)
# 查询 index count  in
# 返回找到的次数,如果没有,返回0 
print("count",list1.count(1))
# 返回索引值,如果没有,报错
print("index",list1.index(50))
# 返回True False
print(50 in list1)

print("list1:",list1)
list1.reverse()
print("list1:",list1)
