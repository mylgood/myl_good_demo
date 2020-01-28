"""
方式一: %占位符来表示字符串中的变量
%s 字符串 %d 整数 %f 小数
name = "lucy"
age = 19
# print("my name is " + name)
# 使用占位符%s的方式 如果有两个属性占位符, 使用%(变量1,遍历2)
print("my name is %s,I am %d"%(name,age))
job = "IT"
print("my job is %s, your job is %s"%(job,job))
# %.2f 保留两位小数
print("this number is %.2f"%3.1415926)

方式二: format函数
"""
name = "lucy"
age = 19
# 使用的而是位置占位符,如果没有写位置, 默认是从0 开始计算
# text = "my name is {0},I am {0}".format(name,age)
# text = "my job is {0}, your job is {0}".format("IT")
# print(text)
# 使用名称占位符
text = "my name is {name},I am {age}".format(name = "jack",age = 18)
print(text)







