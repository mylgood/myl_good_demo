import math
class my_math(object):
    def __init__(self,name):
        self.name = name
    def my_sum(self,a):
        s = 0
        for i in a:
            s += i
        return s

    def add(self,a,b):
        return a+b
    def cos(self,a):
        return math.cos(a)
    def __repr__(self):
        return self.name
# a = [1,2,3]
# ma = my_math("mylll")
# print(ma)
# print(ma.add(1, 2))
# print(ma.my_sum(a))