t1 = (1,2,3)
print(t1 + (4,5,6))
print(t1*3)
# count()
print(t1.count(1))
print(t1.index(1))
for item in t1:
    print(item)
    
print("="*40)
# 元组的装包和拆包
# 在赋值符号右边 会把多个值包装为一个元组
a = 3,4,5
print(a)
print(type(a))
# 把一个元组拆分两个值赋值给a,b
# 在元组拆包的时候,变量的个数必须和元组的数据个数一致
a,b,c = (3,4,5)
print(a)
print(b)
