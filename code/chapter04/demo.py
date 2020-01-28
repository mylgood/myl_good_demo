"""
票务关系系统
每张车票拥有的信息: 
    {"开始站点":"广州","目的站点":"北京","日期":"20190909","票价":800,"数量":100}
① 查询所有的车票信息
② 根据开始站点,目的站点,出行日期查询车票信息
③ 购买车票
④ 退票 
"""

# 初始化车票信息
tickets =[
    {"开始站点":"广州","目的站点":"北京","日期":"20190909","票价":800,"数量":100},
    {"开始站点":"北京","目的站点":"广州","日期":"20190910","票价":800,"数量":100},
    {"开始站点":"广州","目的站点":"上海","日期":"20190909","票价":600,"数量":100},
    {"开始站点":"上海","目的站点":"广州","日期":"20190910","票价":600,"数量":100}
]

def print_menu():
    print("="*50)
    print("1 查询所有的车票信息")
    print("2 根据开始站点,目的站点,出行日期查询车票信息")
    print("3 购买车票")
    print("4 退票")
    print("5 退出系统")
    print("="*50)

# 打印菜单
print_menu()

# 查询所有的车票信息
def list_all():
    print("*"*50)
    for ticket in tickets:
        print(ticket)
    print("*"*50)
# 2 根据开始站点,目的站点,出行日期查询车票信息
def find_by_param(start,end,date):
    for ticket in tickets:
        if start ==ticket['开始站点'] and end ==ticket["目的站点"] and date == ticket["日期"]:
            #返回找到的车票信息
            return ticket
    return None
# 3 购买车票
def buy_ticket(start,end,date):
        ticket = find_by_param(start,end,date)
        if ticket is None:
            print("没有找到对应的车票信息")
        elif ticket["数量"] ==0: 
            print("车票不足:{}".format(ticket))
        else:
            print("购票成功")
            ticket["数量"] -= 1
# 4 退票
def return_tickte(start,end,date,price):
        ticket = find_by_param(start,end,date)
        if ticket is None:
            tickets.append({"开始站点":start,"目的站点":end,"日期":date,"票价":price,"数量":1})
        else:
            ticket["数量"] += 1
        print("退票成功")    
while True:
    model = int(input("请输入你选择的操作序号"))
    if model == 1:
        list_all()
    elif model == 2:
        start = input("请输入开始站点")
        end = input("请输入目的站点")
        date = input("请输入操作日期")
        ticket = find_by_param(start,end,date)
        if ticket is None:
            print("没有找到对应的车票信息")
        else: 
            print("车票信息:{}".format(ticket))
    elif model == 3:
        start = input("请输入开始站点")
        end = input("请输入目的站点")
        date = input("请输入操作日期")
        buy_ticket(start,end,date)
    elif model == 4:
        start = input("请输入开始站点")
        end = input("请输入目的站点")
        date = input("请输入操作日期")
        price = int(input("请输入票价"))
        return_tickte(start,end,date,price)
    elif model == 5:
        break
    else:
        print_menu()
        print("输入的操作有误,请重新输入")
        


    

