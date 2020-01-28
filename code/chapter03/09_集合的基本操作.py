# set 集合 
# 没有顺序 不允许元素重复
# 创建一个集合set
s1 = {1,2,4,3}
print(type(s1))
print(len(s1))
# 报错
# print(s1[0])
print(s1)
print("="*50)
# 不允许元素重复
s2 ={1,2,1,3,1,4}
print(s2)

list1 =[1,2,1,100,200]
s3 = set(list1)
print(s3)
print(list(s3))
# 创建空集合的方式
s4 = set()
print(type(s4))
