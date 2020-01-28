"""
循环结构: 一些代码需要不断重复的去执行
    一直不停的说我爱你
    print("我爱你")
    print("我爱你")
    print("我爱你")
    print("我爱你")
    print("我爱你")
while 条件:
    语句1 
    语句2
"""
# 只需要说100遍 我爱你
start = 0
print("---start---")
while start < 100:
    print("我爱你%d"%start)
    #次数加1
    start += 1
print("---end---")











