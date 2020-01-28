class Person:
    # 定义类属性
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.count = 200
        Person.count = Person.count + 1

    @classmethod
    def get_count(cls):
        # cls 代表当前的类, 方法调用的时候,不需要传递参数
        return cls.count

    @staticmethod
    def main():
        p1 = Person("lucy", 16)
        p2 = Person("marry", 18)
        print(Person.get_count())
        print(p1.get_count())


Person.main()
