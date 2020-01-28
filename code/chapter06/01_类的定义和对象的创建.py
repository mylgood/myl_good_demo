"""
def fn():
    函数体
    [return 值]
fn()
类的定义:
class 类名:
    pass

类名: 首字母大写, 驼峰命名(两个单词连接,每个单词的首字母都需要大写 PersonDemo)
模块名称:英文小写
函数名称: 英文小写,多个单词之间使用_
"""


# 定义一个人类 Person
class Person:
    pass


# 创建一个对象 类名()
p1 = Person()
print(p1)
# 打印id 信息
print(hex(id(p1)))

# 在创建一个对象
p2 = Person()
print(p2)

# isinstance 判断一个对象是否属于某一个类 返回一个布尔值
print(isinstance(p2, Person))
