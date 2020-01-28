"""
复合运算符
x+=y ==> x = x+y
关系运算符 返回结果是布尔值 True False
== : 判断类型,值是否相等
逻辑运算符: 对于所有的对象数据都可以转换为布尔类型
    逻辑与: and 
    逻辑或: or
    逻辑非: not
x and y: 如果X为False的值,那么返回x,否则返回y  返回第一个为False的值,或者说最后一个值
x or y : 如果X为True的值, 那么就返回x,否则就返回y, 返回第一个为True的值,或者是最后一个值
not x: x 为True的值,返回False 否则返回True
"""
num = 100
print(num)
num += 1 # num = num +1  
print(num)
text = "100"
flag =True

print(num == text)
print(flag == 1) # True

print("="*50)
print(0 and 100)
print("wolf" and 300)
print("text" or 0)
# 所谓空字符, 长度为0 的字符
print("="*50)
print(not "") # True
print(not " ")# False
print(not True)#False
print(not 0) #True
