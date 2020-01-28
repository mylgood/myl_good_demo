"""
while: 通用的一种循环方式
for: 通常情况是用来循环遍历序列(字符串,列表,元组,集合...) 可迭代对象
需求: 字符串wolfcode  依次遍历打印出来
    # 需要循环的次数
    length = len(text) # 8
    # 开始循环的位置
    start = 0
    print("--start---")
    while start < length:
        print(text[start])
        # 索引值自增1
        start += 1
    print("--end---")
for 循环: 格式
for item in 字符串:
    print(item)
"""
text = "wolfcode"
print("--start---")
for item in text:
    print(item)
print("--end---")

    








 











