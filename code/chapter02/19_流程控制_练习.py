"""
    输入用户名,密码 
    后台的用户名admin 密码 123456
    如果用户名密码正确,登录成功
    如果只用户名错误,提示用户名错误
    如果只密码错误,提示密码错误
    否则: 用户名和密码都错误
"""

username = input("请输入用户名")
password = input("请输入密码")
if username == "admin" and  password == "123456":
    print("登录成功")
elif username == "admin":
    print("密码错误")
elif password == "123456":
    print("用户名错误")
else:
    print("用户名和密码都错误")









