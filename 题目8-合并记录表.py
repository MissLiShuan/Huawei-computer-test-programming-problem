'''
题目描述
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
 
输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）

示例1 
输入
4
0 1
0 2
1 2
3 4

输出
0 3
1 2
3 4
'''
a = input()
d = {}
for i in range(int(a)):
    b = list(map(int, input().split(' ')))
    if b[0] not in d.keys():
        d[b[0]] = b[1]
    else:
        d[b[0]] += b[1]

for key in d.keys():
    print(key, d[key])
#笔记1###################map()#################################################
'''
描述
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

语法
map() 函数语法：
map(function, iterable, ...)

参数
function -- 函数
iterable -- 一个或多个序列

返回值
Python 2.x 返回列表。
Python 3.x 返回迭代器。

实例
以下实例展示了 map() 的使用方法：
>>>def square(x) :            # 计算平方数
...     return x ** 2
... 
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
 
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]
'''
