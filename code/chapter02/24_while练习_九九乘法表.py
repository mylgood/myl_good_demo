"""
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
"""
line = 1
# 控制行数
while line <= 9:
    start = 1
    while start <= line:
        print("%d*%d=%d"%(start,line,start*line),end="\t")
        start += 1
    print()
    line += 1 # 2






 











