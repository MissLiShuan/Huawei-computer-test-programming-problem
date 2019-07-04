'''
题目描述
Jessi初学英语，为了快速读出一串数字，编写程序将数字转换成英文：
如22：twenty two，123：one hundred and twenty three。
 
说明：
数字为正整数，长度不超过九位，不考虑小数，转化结果为英文小写；
输出格式为twenty two；
非法数据请返回“error”；
关键字提示：and，billion，million，thousand，hundred。
 
方法原型：public static String parse(long num) 
 
 
 
输入描述:
输入一个long型整数
输出描述:
输出相应的英文写法

示例1 
输入
2356

输出
two thousand three hundred and fifty six
'''
def dps(n):
    m1 = 'one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')
    m2 = 'twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')
    if(n<20):
        return m1[n-1:n]#如果n<20则转换成m1[n-1]
    if(n<100):#如果20<n<100
        return [m2[n//10-2]] + dps(n%10)
    if(n<1000):
        return [m1[n//100-1]]+['hundred']+['and']+dps(n%100)
    else:
        for w,p in enumerate(('thousand','million','billion'),1):
            if(n<1000**(w+1)):
                return dps(n//(1000**w))+[p]+dps(n%1000**w)
def question():
    n = int(input())
    return ' '.join(dps(n)) or 'zero'
while(True):
    try:
        print(question())
    except:
        break

#笔记###################################################
'''
Python enumerate() 函数

描述
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
Python 2.3. 以上版本可用，2.6 添加 start 参数。
语法
以下是 enumerate() 方法的语法:
enumerate(sequence, [start=0])
参数
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
返回值
返回 enumerate(枚举) 对象。

实例
以下展示了使用 enumerate() 方法的实例： 
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
普通的 for 循环
>>>i = 0
>>> seq = ['one', 'two', 'three']
>>> for element in seq:
...     print i, seq[i]
...     i +=1
... 
0 one
1 two
2 three
for 循环使用 enumerate
>>>seq = ['one', 'two', 'three']
>>> for i, element in enumerate(seq):
...     print i, element
... 
0 one
1 two
2 three
'''
