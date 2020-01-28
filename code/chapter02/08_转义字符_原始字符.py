"""
转义字符:转义序列可以让我们在在字符串中表示不容易通过键盘输入或者是在输入过程中字符本身有一些特殊意义的,我们需要使用转义字符来表示,
\n 表示的意思是换行
转义字符: \+固定的字符
比如说: 
\' 单引号 普通的字符串,不在是字符串的边界标记
\" 双引号 普通的字符串,不在是字符串的边界标记
\n 换行符 输入换行符
\t 制表符 
\r 回车,返回到当前行最开始的位置
\\
"""
text = "abc\nmp"
# 问题: text 有多少个字符, len()
print(text)
print(len(text)) #6

text2 ='abc\'\"mmp'
print(text2)
text3 = "abc\tdef"
print(text3)
# \r 返回当当前行最开始的地方
print("abcjj\r呵呵哈哈")
print("abc\\tdef")

# filename = "d:\\name\\text2.txt"
# 在字符串前面加上r 代表原始字符串 raw 不在具有转义符号的意义
filename = r"d:\name\text2.txt"
print(filename)

