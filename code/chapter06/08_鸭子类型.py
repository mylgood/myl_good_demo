class Person(object):
    def eat(self):
        print("南方人喜欢吃米饭")


class Dog(object):
    def eat(self):
        print("狗改不了吃屎")


class Cat(object):
    pass


def duck(person):
    person.eat()


def main():
    p1 = Person()
    duck(p1)
    d1 = Dog()
    duck(d1)
    c1 = Cat()
    duck(c1)


main()