"""
老贾造车:
  造车  ---> 返回 {"name":"FF9001","speed":260}
  驾驶  ---> 把车的信息传入到驾驶的功能里面
"""


def make_car(name, speed):
    """
    :param name: 型号
    :param speed: 最高时速
    :return: 返回造好的车
    """
    print("老贾造车")
    return {"name": name, "speed": speed}


def drive(car):
    print("老周驾驶老贾造的%s车,最高时速%s" % (car["name"], car["speed"]))


def main():
    # 造车
    car = make_car("FF9001", 290)
    # 驾驶
    drive(car)


main();
