"""
票务管理系统
优化: DRY 抽取重复代码
在购票,退票,查询的时候,都需要查询车票信息 
对于每个功能的抽取, 把每个功能抽取为单独的函数
"""
# 初始化数据
tickets =[
{'开始站点': '广州', '目的站点': '北京', '日期': '20190909', '票价': 800, '数量': 100},
{'开始站点': '北京', '目的站点': '广州', '日期': '20190910', '票价': 800, '数量': 100},
{'开始站点': '广州', '目的站点': '上海', '日期': '20190909', '票价': 600, '数量': 100},
{'开始站点': '上海', '目的站点': '广州', '日期': '20190910', '票价': 600, '数量': 99}
]

# 打印菜单信息
def print_menu():
    print("="*50)
    print("1 查询所有的车票信息")
    print("2 根据开始站点,目的站点,出行日期查询车票信息")
    print("3 购买车票")
    print("4 退票")
    print("5 退出系统")
    print("="*50)

# 查询所有的车票信息
def query_all():
    for ticket in tickets:
        print(ticket)

# 查询车票信息
def query_ticket(start,end,date):
        for ticket in tickets:
            if ticket["开始站点"] == start and ticket["目的站点"] == end and ticket["日期"] == date:
                # 返回对应的票务信息,结束当前函数的运行
                return ticket
                
# 购买车票
def buy_ticket(start,end,date):
    ticket = query_ticket(start,end,date)
    if ticket is not None:
            if ticket["数量"] > 0 :
                print("购票成功")
                ticket["数量"] -=1
            else:
                print("余票不足")
    else: 
        print("没有对应的票务信息")
        
# 退票
def return_ticket(start,end,date,price):
    ticket = query_ticket(start,end,date)
    if ticket is not None:
        ticket["数量"] +=1
    else: 
        tickets.append({'开始站点': start, '目的站点': end, '日期': date, '票价': price, '数量': 1})
    print("退票成功")
# 对于功能上是重复的代码使用循环
# 给程序定义一个入口
def main():
    print_menu()
    while True:
        model = input("请输入你选择的操作序号")
        if model == "1":
            query_all()
        elif model == "2":
            start = input("请输入开始站点")
            end = input("请输入目的站点")
            date = input("请输入出发日期")
            ticket = query_ticket(start,end,date)
            if ticket is not None:
                print("车票信息",ticket)
            else: 
                print("没有对应的票务信息")
        elif model == "3":
            start = input("请输入开始站点")
            end = input("请输入目的站点")
            date = input("请输入出发日期")
            buy_ticket(start,end,date)
        elif model == "4":
            start = input("请输入开始站点")
            end = input("请输入目的站点")
            date = input("请输入出发日期")
            price = input("请输入票价")
            return_ticket(start,end,date,price)
        elif model == "5":
            break
        else:
            print("输入有误,请重新输入")
            
main()
