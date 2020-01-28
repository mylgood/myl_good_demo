import log
import time
import random
import sys
# 模块的查找 首先当前项目,如果找不到,依次去sys.path中指定的目录中查找

if __name__ == '__main__':
    log.fun01()
    # 让程序暂停2s
    time.sleep(0.1)
    print(123)
    # 查看模块的具体位置
    print(random.__file__)
    print(log.__file__)
    print("*"*50)
    # 在sys中的path就指定了模块查找的相关路径
    for item in sys.path:
        print(item)
