"""
函数的定义:
    def 函数名([参数1,参数2,...,参数n]):
        函数体
        [return 值]
    分类:
    ① 无参数无返回值
    ② 无参数有返回值
    ③ 有参数无返回值
    ④ 有参数有返回值
"""
# 无参数无返回值
def talk():
    print("好好学习,天天向上")
    
talk()

# 无参数有返回值
def get_time():
    return "20190909"
ret = get_time()
print("时间:",ret)

# 有参数无返回值
def insert(record):
    print("插入数据{}成功".format(record))
    # return None   

insert(123) # recode = 123

# 有参数有返回值 求和
def get_sum(x,y):
    print(x,y);
    return x+y
    
ret =get_sum(11,12)
print("结果:",ret)




    

