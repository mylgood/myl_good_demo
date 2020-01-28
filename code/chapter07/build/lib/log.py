# 申明导入的模块 只对 from log import *
__all__ = ["fun01", "fun02"]


def fun01():
    print("...log...fun01...")


def fun02():
    print("...log...fun02...")


def add(*args):
    """计算多个数据的和,并且返回"""
    value = 0
    for item in args:
        value += item
    return value


if __name__ == "__main__":
    fun01()
    fun02()
    ret = add(1, 2, 3, 4, 5)
    print(ret)
    # __name__ : 如果作为主程序运行 其中值是__main__
    # 如果是作为模块导入到其他程序中使用, name这个值是 模块名 log
    print("log魔法属性name:", __name__)

