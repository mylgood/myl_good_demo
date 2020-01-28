# 不定长参数
def fun_a(x,y,z):
    print(x,y,z)
    
    
#fun_a(1,2,3,4,5,6)
# print(sum(1,2))

def sum(x,*args,y):
    print("args",args)
    print("x:",x)
    print("y:",y)
    #return x+y+z
# 存在需求: 在定义函数的时候,不能确定传入的实际参数个数
# 不定长参数 *args 代表可以接受多个非关键字参数
# 如果在*args前面的参数,可以通过位置参数赋值方式,如果是在*args后面的参数,必须接受关键字参数
# print(sum(1,2))
# sum(1,2,3,4)
# sum(x=1)
# *args 可以接受0 或多个非关键字参数 
sum(1,2,y=3)

print("*"*40)
#必须使用关键字参数传递,而且只能是3个参数 
# 当只使用* 代表后面的必须是关键字参数,而且参数个数必须相对 * 不能接受其他擦书
def fun_b(*,x,y,z):
    print("x:{},y:{},z:{}".format(x,y,z))
    
fun_b(9,x=1,y=2,z=3)