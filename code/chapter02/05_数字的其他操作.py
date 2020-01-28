"""
表达式操作 
 + - * / 
 x//y 整除 去x除以y的取整数部分
 x%y  取余数 x除以y的余数部分
 x**y
 
 pow(x,y)==> x**y x的y次方
 abs(x) ==> |x| 返回的是x的绝对值
 random 是一个python中内置的模块,需要通过import 导入模块
"""
# 导入random模块
import random
# / 返回一个小数类型的数据
print(-5/2) # -2.5
print(-5//2)# -3 
print(5%2)
print(5*2)
# 求5的平方
print(5**2)
print(pow(5,2))
print(abs(-2))
# int 可以把字符串转换为数字
# 100 
print(int("100")) # 100
print(int("100",2)) # 4
print(int("100",16)) # 4
print("===================")
# 生成一个1-10之间的随机数
print(random.randint(1,10))
# dir 显示模块有哪些方法可以使用
print(dir(random))
# help 查看方法的的帮助文档
print(help(random.randint))
