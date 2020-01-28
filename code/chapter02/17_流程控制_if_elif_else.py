"""
如果需要有超过2个结果需要处理,我们需要使用多个条件表达式进行判断
格式:
if 表达式1 :
    语句1
elif 表达式2 :
    语句2
else:
    语句3 
需求: 订单金额 > 128 EMS包邮 
      订单金额 > 68  韵达包邮
      否则:   邮费自理
"""
amount = int(input("请输入您的订单金额"))
print("---start--")
if amount >= 128:
    print("EMS包邮")
elif amount >= 68:  
    print("韵达包邮")
else:
    print("邮费自理")
print("---end---")








