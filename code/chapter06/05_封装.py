class Person:
    def __init__(self, name, age):
        # 在所有的属性名称以一个下划线 _ 开头的属性, 私有属性 但是私的不够彻底  使用双下划线 保证属性的彻底私有化
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        self.__test1()
        return self.__age

    def set_age(self, age):
        if age <= 0:
            age = 1
        elif age > 120:
            age = 120
        self.__age = age

    # 私有化方法 方法名称前面加上 双下划线
    def __test1(self):
        print("test1....")


def main():
    p1 = Person("jack", 18)
    # 修改对象的属性 直接访问对象的属性
    p1.set_age(-300)
    print("%s 的年龄: %s" % (p1.get_name(), p1.get_age()))
    # 调用方法


main()
