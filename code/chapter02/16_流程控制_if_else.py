"""
# 条件成立才会去做
if 条件: 
    # 语句1
# 条件成立 做事情1 条件不成,做事情2 

语法格式: 
if 条件表达式:
    语句1
else:
    语句2

需求: 订单金额 > 128 EMS包邮 否则 韵达包邮

"""
# input接受的所有数据都是字符串类型 
amount = int(input("请输入您的订单金额"))
if amount >= 128:
    print("金额超过128")
    print("EMS包邮")
else:
    print("韵达包邮")
 




