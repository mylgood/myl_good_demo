"""
类 概念: 事物的特征和行为的描述
人类:
    特征(属性)
        name : 姓名
        age: 年龄
    行为(方法) 功能
        eat(): 吃放
        sleep(): 睡觉
"""


# 定义一个Person 类
class Person:
    # 定义一个初始化方法,用来设置name和age
    # self: 代表的是当前所创建的那个对象
    def __init__(self, name, age):
        print("init method ")
        self.name = name
        self.age = age

    # 类的一个普通的方法, 定义格式和函数一样,区别: 必须有一个参数self
    def eat(self):
        print(self)
        print("吃饱喝足,玩好")

    def sleep(self):
        print("好好睡觉...做个美梦")


# 创建对象p1
# p1 --> self
# "张三" -->name
# 18 --> age
p1 = Person("张三", 18)
# 属性方法
print(p1, p1.name, p1.age)
# 调用对象的方法
p1.eat()
p1.sleep()



