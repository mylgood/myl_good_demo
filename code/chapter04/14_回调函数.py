# 回调函数
def send_msg():
    """发送短息"""
    print("亲爱的,我到家了")
    
def go_home(callback):
    """回家
        callback: function 
    """
    print("打出租车回家")
    print("到家了")
    callback()
def eat():
    print("肚子饿了,吃方面面")
    
#go_home(send_msg)
# 函数名称(而不是函数调用)
go_home(eat)
go_home(lambda : print("在和别人去看电影"))