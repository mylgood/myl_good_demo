"""
常量: 在程序中固定不变的值,在初始化后期值不会发生改变,
通常情况指的是我们所创建的对象
数字: 1 ,3,14 100
字符串: "python","wolfcode","ooxx"
变量:指的是存放数据的一个容器（盒子）
特点：　
①　给变量一个名字，叫做变量名，区分大小写，符合标识符的命名规范
②　变量定义的时候需要给其赋值，不赋值的变量是不能调用
③  对于变量来说,是没有数据类型,但是对于变量中所存放的对象,是有数据类型
    可以通过type函数查看对象的类型
④  如果一个变量去参与表达式的运算的话,那么实际上是变量中的对象数据去参与运算

"""
username = "jack"
# usernName="lucy"
# type(变量名) : 查看变量所存放的对象的数据类型
print(type(username))
print(username)
username = 18
print(type(username))
print(username)
# 那username中的数据对象18 去参与运算
print(username+5)
# 给变量a 赋值3 给变量b 赋值4 
a,b = 3,4
print(a,b)
