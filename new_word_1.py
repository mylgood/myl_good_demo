"""
from new_word import my_math

a = [1,2,3]
ma = my_math("mylll")
print(ma)
print(ma.add(1, 2))
print(ma.my_sum(a))
"""
# import sys
# print(help(sys))
# import time
# s = time.time()
# from new_word import my_math
#
# a = range(100000000)
# ma = my_math("mylll")
# print(ma.my_sum(a))
# print(time.time() - s)
# import os
# for i in os.listdir("F:\\MyFiles\\论文or课件\\1990~2019 ICCV最佳论文汇总"):
#     print(i)
# 马艳龙 = "sb"
# print(马艳龙)
# import urllib3
# http = urllib3.PoolManager();
# r = http.request('get', 'http://www.baidu.com/s', fields={'wd': '周杰伦'})
# print(r.data.decode())
"""
a = 1
b = 0

try:
    # print(a/b)
    assert 1!=1
    # raise ImportError
except ZeroDivisionError as e:
    print(e)
except AssertionError as e1:
    print(e1)
finally:
    print("dddd")
"""
# a = open("b.txt","r",encoding="utf-8")
# print(a.readlines())
# b = open("c.txt","w")
# b.write("hello world!!!")
# b.close()
import os
# os.remove("c.txt")
os.rename("c.txt","myl.txt")