"""
老贾造车:
  造车  ---> 返回 {"name":"FF9001","speed":260}
  驾驶  ---> 把车的信息传入到驾驶的功能里面

对象分析:
    老贾
        name
        age
        make_car()
        drive()
    电动汽车
        name 型号
        speed 最高时速
        run() 汽车行驶
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_car(self, name, speed):
        print("%s造册"%self.name)
        # 创建一个车的对象
        car = ElectricCar(name, speed)
        return car

    def drive(self, car):
        car.run()
        print("%s开着%s车,最高时速是%s" % (self.name, car.name, car.speed))


class ElectricCar:
    def __init__(self,name, speed):
        self.name = name
        self.speed = speed

    def run(self):
        print("小电动车在公路上行驶....")


def main():
    # 创建Person对象 老贾
    laojia = Person("laojia", 34)
    car = laojia.make_car("FF9001", 280)
    # print("电动车信息:{'name':%s,'speed':%s}" % (car.name, car.speed))
    laojia.drive(car)


main()




