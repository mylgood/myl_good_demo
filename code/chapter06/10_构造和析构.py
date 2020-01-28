import time


class Student:
    # 创建对象
    def __new__(cls, *args, **kwargs):
        print("student ... new...")
        obj = object.__new__(cls)
        return obj

    # 初始化赋值操作
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("student ... init ...")

    # 在程序结束的时候,释放资源 或者被当做垃圾回收的时候
    def __del__(self):
        print("student ... del ...")

    @staticmethod
    def main():
        s1 = Student("marry", age=16)
        print(s1)
        print("...end ...")


Student.main()