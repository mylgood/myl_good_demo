"""
数值类型: 整数(int) 和小数(float),复数
① 数值是不可变类型的对象
② 数值的表示方式 十进制, 十六进制 八进制 二进制
③ 数据之间的进制转换hex() oct() bin() int()

"""
# 十进制
num1 = 100
print(num1)
# 十六进制
num2 = 0xff
print(num2)
# 八进制
num3 = 0o75 # 5*8^0 + 7*8_^1
print(num3)
# 二进制 
num4 = 0b101 # 1+0+4 5
print(num4)
# 进制之间的转换
num5 =6890
print(num5)
# bin(num) 使用二进制表示数据
print(bin(num5))
# hex(num) 使用十六进制表示
print(hex(num5))
# oct(num) 使用八进制表述
print(oct(num5))
# 怎么把一个八进制数据转换为十进制
print(int(0o77))
# 把字符串转换为数字必须是一个符合条件的数字
print(int("109"))



