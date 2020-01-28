"""

"""


# 虽然没有写继承关系,默认情况继承object
class Person(object):
    def __init__(self, name, age):
        print("Person....init ....")
        self.name = name
        self.age = age

    def eat(self):
        print("%s吃饭...."% self.name)

    def sleep(self):
        print("%s准备睡觉"% self.name)


#  学生类 继承 person 类
class Student(Person):
    def __init__(self, name, age, sn):
        print("Student....init ....")
        # self.name = name
        # self.age = age
        # 调用父类的初始化方法 super() 代表调用父类对象的方法
        super().__init__(name, age)
        self.sn = sn

    def eat(self):
        #super().eat()
        print("作为学生,我们应该多吃粗粮,可以长身体")





def main():
    # 执行父的初始化方法
    s1 = Student("marry", 21,"0001")
    print(s1.name, s1.age, s1.sn)
    s1.eat()


main()

