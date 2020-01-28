"""
图书管理系统
图书的信息 书名,数量
主要功能
① 根据书名查找图书
② 借阅图书
③ 归还图书
④ 显示所有图书
"""
# 一个图书信息使用一个字典来表示 {"书名":"Python实战","数量":10}
# 初始化数据
books =[
    {"书名":"python","数量":10},
    {"书名":"java","数量":10},
    {"书名":"redis","数量":10}
]
print("*"*50)
print("图书管理系统")
print("1 查找图书")
print("2 借阅图书")
print("3 归还图书")
print("4 显示所有图书")
print("5 退出系统")
print("*"*50)
while True:
    opt = int(input("请输入你的选择序号"))
    if opt == 1:
        item = input("请输入你查找的图书名:")
        for book in books:
            if book["书名"] == item:
                print("您要找的图书信息:",book)
                break
            # 当在循环中使用了break 跳出循环的时候,不会执行该操作
        else:
            print("没有你要找的书籍:%s"%item)
    elif opt == 2:
        item = input("请输入你借阅的图书名:")
        for book in books:
            if book["书名"] == item and book["数量"] > 0:
                book["数量"] -= 1
                print("借阅成功")
                flag = True
                break
        else:
            print("没有你要借阅的书籍:%s"%item)
    elif opt == 3:
        item = input("请输入你归还的图书名:")
        for book in books:
            if book["书名"] == item:
                book["数量"] += 1
                print("归还成功")
                break
        else:
             books.append({"书名":item,"数量":1}) 
    elif opt == 4:
        print("="*50)
        for book in books:
            print(book)
        print("="*50)
    elif opt == 5:
        break
    else:
        print("您输入的有误,请重新输入")








