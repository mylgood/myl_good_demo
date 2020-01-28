"""
x.find(y) 在字符串x中查找y,如果找到,返回第一次找到对应的索引值,如果没有找到,返回-1
    text = " good good study day day up"
    num = text.find("ooxx")
    print(num)
x.index(y) 在字符串x中查找y,如果找到,返回第一次找到对应的索引值,如果没有找到,直接报错ValueError
    text = " good good study day day up"
    num = text.index("0011")
    print(num)
替换: 
x.replace(y,z) 把字符串x中的y替换为z,替换完以后返回一个新的字符串,原来的字符串不会改变
    x = " I am good boy"
    text  = x.replace("good00","bad")
    print(x)
    print(text)
#字符串分割
x.split([y]) 把字符串x 按照y进行分割
#字符串合并
y.join(x):用字符y把x中的而每个数据连接起来

x.strip(): 把x字符串的两边的空格去掉

x.encode("utf-8")  把字符串编码为字节数据(前面有一个字符b),参数为编码规则,默认情况就是utf-8
y.decode("utf-8")  把字节数据解码为字符串数据,注意的是编码规则一定要一致 
"""
# split 可以把一个字符串拆分多个字符串
x = "你好,谢谢,对不起,请,再见"
text2 = x.split(",")
print(text2)
print(x)

text3 = "$".join(text2)
print(text3)

x = "   wolf code  ,color wolf   "
text4 = x.strip()
print(x)
print(text4)
print("="*50)
x = "hello"
y = x.encode("utf-8") #b'hello'
print(x)
print(y)
print(type(x))
print(type(y))
# 把字节数据转换为字符数据
z = y.decode("utf-8")
print(z)






 






