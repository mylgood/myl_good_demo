"""
操作流程
① 创建一个数字对象100
② 创建一个变量a
③ 把100赋值给变量a
"""
a = 100
# 在表达式中a ==> 数据替换
print(a)# 100
# id(a) 判断变量a中所存放的内存地址值
print(id(a))
a = 108
# 不可变对象: 数字,字符串 不可变对象,不能改变已经创建的对象的值
print(a) # 108
print(id(a))