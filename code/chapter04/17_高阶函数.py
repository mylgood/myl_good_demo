'''
def fun_a(callback):
    """
    callback:function
    """
    callback()
    return 1

def fun_b():
    print("fun_b")
    
    
fun_a(fun_b)

def fun_c():
    print("fun_c")
    return fun_b
    
ret = fun_c()

print(ret)
ret()
'''
# map 是一个映射, 接受两个参数,第一个参数是一个函数,第二个参数是序列(列表/元组)
# 返回值: 可迭代的对象 list(ret) 转换为序列
#需求: 有一个列表[1,2,3,4,5] 给 每个元素都加上10,并且生成一个新的列表
list_a = [11,12,13,14,15]
list_c = [31,32,33,34,35]
list_b = []
# 思考一个问题: 对于list_b 中的额数据 由list_a中的数据,根据一个规则生成得出
"""
for item in list_a:
    list_b.append(item+10)
    
print("list_b",list_b)
"""
fn = lambda x : x+10
# 返回值是一个可迭代对象 list(ret) 可以转换为列表
ret = map(fn,list_a)
print("list_b",list(ret))

ret = map(lambda x,y:x+y,list_a,list_c)
# 通过list函数转换为列表
print("list_c",list(ret))

