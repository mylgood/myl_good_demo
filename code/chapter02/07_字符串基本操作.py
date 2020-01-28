"""
字符串: 使用引号括起来的文字, 通常情况表达的是文字的信息,有序的字符集合
① 使用单引号
② 使用双引号
③ 使用三重引号  可以对字符串换行
如果你使用单引号或者双引号的时候表示的字符串需要换行,在结尾加上转义字符\

字符串的特点: 
① 有序的字符集合 字符串ab 和字符串ba 是不同的字符串
② 对于字符串中的每个字符都有一个对应的索引,从左往右, 从0 开始 text[0]
    索引特点: 从左往右 从0开始 从右往左 从-1开始 通过索引可以找到字符串中的一个字符
③ 对于字符串是不可变对象 数字一样
④ 对于字符串的长度len()方法查看
⑤ 同str()函数可以把其他对象转换为字符串对象  int()
⑥ + * 
"""
text = 'python'
print(text)
# type(text) 查看对象的类型
print(type(text))

text2 = "wolfco\
de"
print(text2)

text3 = """呵呵OAOA
新的一行
再来一行
"""
print(text3)
print(type(text3))

print("===============")
# 索引访问 text的第一个字符
print(text[0])
# 报错, 超出索引范围
# print(text[300])
# 最后一个元素
print(text[-1])

# 错误, 不能修改字符串中的字符
# text[-1] = "B"
# print(text[-1])
# text = "java"
# 0 5 
print(len(text))
print(text[len(text)-1])
# len(text)-1 代表最后一个元素的索引
# text[len(text)-1]
print(str(123455))
print(type(str(123455)))

print("==加法和乘法==")
# 字符串连接符号 连接的必须是字符串
print("ptyhon" + "java")
print("123" + str(456))
print(int("123") + 456)
# 乘法操作
print("="*50)