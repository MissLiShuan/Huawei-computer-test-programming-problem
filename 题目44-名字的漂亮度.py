'''
题目描述
给出一个名字，该名字有26个字符串组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。 
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个字母拥有相同的“漂亮度”。字母忽略大小写。 
给出多个名字，计算每个名字最大可能的“漂亮度”。 
输入描述:
整数N，后续N个名字
输出描述:
每个名称可能的最大漂亮程度

示例1 
输入
2
zhangsan
lisi

输出
192
101
'''
while(1):
    try:
        a = int(input())#整数a，后续a个名字
        b,result = [],[0]*a#b = [],result = [0,0]共2个
        for i in range(a):
            b.append(input())#该循环输入名字b=['zhangsan','lisi']
        for i in range(a):
            c = set(list(b[i]))#i=0时c={'n', 'h', 'a', 'g', 's', 'z'},i=1时，c={'s', 'l', 'i'}
            d= []
            for j in c:
                d.append(b[i].count(j))#b[i].count(j)计算，zhangsan中有几个n，h,a,g,s,z
                d.sort(reverse = True)#将d降序排序
            for k in range (len(d)):
                result[i] = result[i]+d[k]*(26-k)
                print(result)
        for i in range(a):
            print(result[i])
    except:
        break
