"""
# 需求 把字符串中的字符转换列表中的每个元素
text = "wolfcode"
list1 = list(text)
print(list1)
"""
text = "wolfcode"

"""
list1 = []
for item in text:
    list1.append(item)
# 列表推导式
list1 =[ item for item in text]
print(list1)

# MF  SMLX
list2 = []
for sex in "MF":
    for size in "SMLX":
        list2.append(sex+size)
print(list2)
"""
# 衣服的型号
list2 =[ sex+size for sex in "MF" for size in "SMLX" if not (sex =="F" and size =="X")]
print(list2)




