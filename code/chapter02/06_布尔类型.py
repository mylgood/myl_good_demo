"""
布尔类型: 只有两个值True,False 布尔类型是整数类型(int)的子类
其中特点:
① 可以和整数直接参与运算
② 如果把True,False转换为数字 True --> 1 False -->0
③ 数字可以转换为布尔类型 0 --> False, 非0 --> True bool(num)
④ 在Python中所有的数据都可以表示为True,False 
    在字符串中, 空字符表示False,非空字符表示True  bool(str)
"""
flag = True

print(flag)
# flag --> 1
print(flag+4)
# bool 把一个数字转换为布尔类型
print(bool(0.0))
#True
print(bool(100))
#False
print(bool(""))
#True
print(bool("\n"))

