"""
字符串是一个有序的字符的集合
通过字符串索引 text[-1] 是可以获取到一个字符
如果需要从字符串中获取多个字符的话,就需要用到分片

str[start:end:step]
如果start省略: 默认0 
如果end省略,默认为len(str)
如果step 省略,默认为1 
start: 正整数 负整数
end: 正整数 负整数
step:正数,正偏移,负数, 负偏移
"""
text = "python"
# 需求 截取code字符串出来
text2 = "wolfcode"
# 分片: text2[start:end] start:开始索引,end:结束索引(不包括)
# 分片: 返回一个新的字符串,原来的字符串不会改变
text3 = text2[4:8]
print(text3)
# 如果不写结束索引,默认为字符串的长度len(text2)
print(text2[2:])
# 如果不写开始索引,默认为0 
print(text2[:4])
# 拷贝出一个新的字符串
text4 = text2[:]
print("="*50)
print(text4)
# 步长 默认不写的话 1 
# text2[start:end:step]
# 需求: 索引值为0 2 4 6 8 这样的索引的字符
text5 = text2[::2]
print(text5)
# 需求: 获取python 中的最后三个字符
print(text2[-3:-2])
# 反向打印
print(text2[-1::-1]) 







