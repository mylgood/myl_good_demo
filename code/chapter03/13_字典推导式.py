"""
姓名,数学成绩,英语成绩,语文成绩

方法一:
# 找到所有的key
keys = d1.keys()
print(keys)
for key in keys:
    print("{0}-->{1}".format(key,d1[key]))
    
# 通过循环的方式打印d1的所有信息
#方法二
items = d1.items()
print(items)
for key,value in items:
    print("{0}-->{1}".format(key,d1[key]))
"""
d1 = {"姓名":"张三","数学":90,"英语":80,"语文":70}
d2 = {"姓名":"李四","数学":60,"英语":95,"语文":90}

# 方法三 对于字典的for 遍历 ,默认情况遍历所有的keys
for key in d1:
    print("{0}-->{1}".format(key,d1[key]))

# 需求 生成1-10 之间所有的数的平方,并且对应起来 {1:1,2:4,3:9...,9:81}
d3 = { key:key**2 for key in range(10)}
print("d3",d3)

 
