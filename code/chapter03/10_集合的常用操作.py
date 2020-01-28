s1 = {1,3,2,4}
s2 = {3,1,8,0}
# list1 = [1,3,2,4]
s1.add(100)
# 在set集合中可以存放不可变的数据,但是对于可变的数据列表list,集合数据set 
s1.add((200,300))
s1.remove(100)
# 随机删除一个元素
# s1.pop()
# 清空数据
# s1.clear()
# 两个集合的交集
s1 = {1,3,2,4}
s2 = {3,1,8,0}
print("交集,",s1 & s2)
# 两个集合的并集
print("并集,",s1 | s2)
# 求差集
print("差集",s1-s2)
print(s1)
print(s2)
# 循环遍历集合
for item in s1:
    print(item)
# 集合推导式 
s3 ={ index for index in range(10) if index%2 ==0}
print(s3)