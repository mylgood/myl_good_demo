class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Student:{'name':%s,'age':%s}" % (self.name, self.age)

    def __len__(self):
        return len(self.name)

    def __call__(self, *args, **kwargs):
        print("1234")
        print("3456")

    @staticmethod
    def main():
        s1 = Student("lucy", 18)
        # 打印 __str__
        print(s1)
        # 对象是有哪个类创建出来
        print(s1.__class__)
        print(Student.__mro__)
        # s1__len__
        print(len(s1))
        # s1.__call__
        s1()


Student.main()