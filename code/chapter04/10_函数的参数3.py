def fun_a(x, y, z,*args,**keywords):
    # args 元组类型
    # keywords 字典类型
    print("args",args)
    print("keywords",keywords)
    print("x:{},y:{},z:{}".format(x,y,z))

# 如果需要接受多个关键字参数 需要使用**keywords,必须放到最后一个参数 
# fun_a(88,x=1,y=2,z=3,key=99,num=900)
# fun_a(88,x=1,y=2,z=3)
fun_a(1,2,3,4,5,6,key=99,num=88)

