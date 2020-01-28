"""
成员关系: 体现的是对象(序列对象 字符串,元组,列表,集合)之间的包含关系
x in y  如果在y中包含x 返回True,否则,返回False
x not in y   如果在y中不包含x 返回True,否则,返回False

实体对象测试:判断两个变量是否存的是同一个对象(共享引用) id(x)==id(y)
x is y 表示x 和y是同一个对象 id(x) ==id(y)  内存地址值,x == y
x is not y 

"""

text1 = "wolfcode"
text2 = "code"
print(text2 in text1) #True
print("ooxx" not in text2) #True
text3 = text1 # "wolfcode"
print("="*10)
print(id(text1))
print(id(text3))
print(text1 is text3 )
print(text1 == text3 )


