# 水栖动物 如果不写,默认继承object类
class AquaticAnimal(object):
    def __init__(self, name):
        self.name = name

    def siwm(self):
        print("在水里面愉快的游泳")

    def sleep(self):
        print("我可以在水里面睡觉,屌不屌")


# 陆栖动物
class TerrestrialAnimal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print("在草原上疯狂的奔跑")

    def sleep(self):
        print("我可以在草原上睡觉")


# 如果是多继承,多个父类之间使用逗号隔开
class Amphilbians(AquaticAnimal, TerrestrialAnimal):
    def sleep(self):
        print("我即可以在水里,也可以在陆地上睡觉,谁厉害...")


def main():
    # 1 创建对象
    a1 = AquaticAnimal("小金鱼")
    a1.siwm()
    a1.sleep()
    print("=" * 50)
    # 2 创建一个陆栖动物
    a2 = TerrestrialAnimal("华南虎")
    a2.run()
    a2.sleep()
    print("="*50)
    # 3 创建一个两栖动物
    a3 = Amphilbians("青蛙")
    a3.run()
    a3.siwm()
    a3.sleep()
    # 获取到方法的解析顺序
    # (<class '__main__.Amphilbians'>, <class '__main__.AquaticAnimal'>, <class '__main__.TerrestrialAnimal'>, <class 'object'>)
    print(Amphilbians.__mro__)


main()

# 如果一个方法在子类中没有,但是在多个父类中存在的话,究竟调用哪个父类里面的方法?  C3