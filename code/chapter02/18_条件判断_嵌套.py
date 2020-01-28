"""
需求: 
    你女朋友需要买一个lv,需要向你借10000
    如果你的卡的余额超过10000 (8000)
        输入密码转账操作
        如果输入的密码正确: 123456
            转账成功
        否则:
            转账失败,密码错误
    否则:
        余额不足
"""
amount = int(input("宝贝,你需要多少钱啊"))
print("---start---")
if amount <= 8000:
    # 语句占位符,
    # pass
    password = input("请输入密码:")
    if password == "123456":
        print("转账成功")
        print("宝贝,钱到账了没呀")
    else:
        print("密码错误")      
else:
    print("钱不够")
print("---end---")









