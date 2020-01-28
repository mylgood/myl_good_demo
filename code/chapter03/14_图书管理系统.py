"""
图书管理系统
1 查找图书  根据书名查找
2 借阅图书  如果借阅成功,对应的图书数量减1
3 归还图书  如果已经有对应的图书,name在原来的基础上加1 否则,新建一个图书信息添加到list列表中
4 显示所有图书  循环遍历list集合信息
5 退出系统   程序结束
一种书的信息使用什么类型的数据来存储  --> 字典类型dict
多种书的信息使用什么类型的数据来存储 ---> 列表list

# list  dict
if for while  break 
"""
print("*"*50)
print("图书管理系统")
print("1 查找图书")
print("2 借阅图书")
print("3 归还图书")
print("4 显示所有图书")
print("5 退出系统")
print("*"*50)

# 所有的图书信息使用列表
books = [
    {"名称":"python","数量":10},
    {"名称":"java","数量":10},
    {"名称":"c","数量":10}
]
while True:
    model = int(input("请输入你的选择序号"))
    if model == 1:
        #print("1 查找图书")
        # 输入需要查找的书名
        book_name = input("请输入需要查找的书名")
        for book in books:
            if book_name == book["名称"]:
                print("找到你需要的图书信息:",book)
                break
        # 循环中的else 一般都是配合break使用,当没有执行break语句时 ,会执行else中的语句
        # 如果执行了break的话,就不会执行else中的语句
        else:
            print("没有找到您需要的书:",book_name)        
    elif model == 2:
        #print("2 借阅图书")
        # 输入需要查找的书名
        book_name = input("请输入需要借阅的书名")
        for book in books:
            if book_name == book["名称"]  and book["数量"] > 0:
                print("借阅成功")
                book["数量"] -= 1
                break
        else:
                print("没有您要借阅的图书:",book_name)
    elif model == 3:
        #print("3 归还图书")
        # 输入需要查找的书名
        book_name = input("请输入需要归还的书名")
        for book in books:
            if book_name == book["名称"]:
                book["数量"] += 1
                break
        else:
            books.append({"名称":book_name,"数量":1})
        print("归还成功")
    elif model == 4:
        print("="*40)
        # 循环遍历图书信息
        for book in books:
            print(book)
        print("="*40)
    elif model == 5:
        print("5 退出系统")
        # 结束循环
        break
    else: 
        print("输入的序号有误")
