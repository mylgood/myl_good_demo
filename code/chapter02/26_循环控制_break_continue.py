"""
break continue 控制循环跳转

需求: 1  请计算100以内最大的5个奇数和
sum = 99 + 97 + 95 + 93 + 91
print(sum)

break: 结束整个循环
continue: 结束本次循环,继续下一次循环判断(在结束本次循环之前,需要改变循环条件)
"""

# 基数个数
count = 0
# 开始的值
start = 100
# 总和
sum = 0
while start > 0:
    # 判断start是否是基数
    if start%2 == 0:
        #结束本次循环
        start -= 1
        continue
    sum += start
    count += 1
    if count  == 5 :
        # 结束循环
        break
    start -= 1
print(sum)







    








 











