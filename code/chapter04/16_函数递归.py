# 需求: 
def sum(x):
    """
     用于计算x整数以内的和
     x: int
     return 1-x之间的所有整数和
    """
    value = 0
    for item in range(1,x+1):
        value += item
    return value
ret = sum(10)
print(ret)
print("*"*80)
def sum2(x):
    value = 0    
    if x > 1 :
        value = x + sum2(x-1)
    else:
        value = 1
    return value;    
ret = sum2(2)
print(ret)