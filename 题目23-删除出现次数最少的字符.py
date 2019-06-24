'''
题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
 
输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。

示例1 
输入
abcdd

输出
dd

'''

while True:
    try:
       l=input()
       a=[]#存放每个字符的计数结果
       for i in l:
           a.append(l.count(i))#l.count(i)对字符进行计数
       result =[]
       min_a = min(a)#z好到出现次数最少的字符个数
       for (i,j) in zip(l,range(len(a))):
           if a[j] != min_a:
               result.append(i)
       print(' '.join(result))      
    except:
        break

#笔记1###############count()函数####################################
'''
描述：统计字符串里某个字符出现的次数。可以选择字符串索引的起始位置和结束位置。           
语法：str.count("char", start,end)  或 str.count("char")    -> int    返回整数

str —— 为要统计的字符(可以是单字符，也可以是多字符)。
star —— 为索引字符串的起始位置，默认参数为0。
end —— 为索引字符串的结束位置，默认参数为字符串长度即len(str)。
程序示例：
str = "i love python,i am learning python"
print(str.count("i")) #star 和end 为默认参数
print(str.count("i",2)) # star值为2，end值为默认参数
print(str.count("i",2,5)) #star值为2，end值为5
print(str.count("am"))  #多字符统计

程序运行结果：

3
2
0
1

描述
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。
如果需要了解 Pyhton3 的应用，可以参考 Python3 zip()。
语法zip([iterable, ...])
参数说明：
iterabl -- 一个或多个迭代器;
返回值
返回元组列表。
实例
以下实例展示了 zip 的使用方法：
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]


join函数
1、join()函数
语法： 'sep'.join(seq)
参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串
 
2、os.path.join()函数
语法： os.path.join(path1[,path2[,......]])
返回值：将多个路径组合后返回
注：第一个绝对路径之前的参数将被忽略
'''
