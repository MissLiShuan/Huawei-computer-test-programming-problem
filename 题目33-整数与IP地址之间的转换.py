'''
题目描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。
 
的每段可以看成是一个0-255的整数，需要对IP地址进行校验
 
 
 
输入描述:
输入 
1 输入IP地址
2 输入10进制型的IP地址

输出描述:
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址

示例1 
输入
10.0.3.193
167969729

输出
167773121
10.3.3.193

'''
def ipToInt(n):#IP地址转换成int整数，输入是IP地址字符串
    a = ''
    for i in range(len(n)):#遍历IP地址字符串
        a += bin(int(n[i]))[2:].rjust(8,'0')#保证工8位，不够的补0，bin(10)>>>'0b1010',因此为[2:]
     
    return int(a,2)#二进制转换成10进制
def IntToIp(n):#int整数转换成IP地址，输入是整数
    a = []
    b = bin(n).replace('0b','').rjust(32,'0')#用''替换‘0b’
    for i in range(4):
        a.append(str(int(b[8*i:8*i+8],2)))
    return a
while True:
    try:
        n = input().split('.')
        m = int(input())
        result1 = ipToInt(n)
        print(result1)
        result2 = IntToIp(m)
        print('.'.join(result2))
    except:
        break

#笔记###############join()方法####################################
'''
笔记1-Python rjust()方法
描述
Python rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
语法
rjust()方法语法：
str.rjust(width[, fillchar])
参数
width -- 指定填充指定字符后中字符串的总长度.
fillchar -- 填充的字符，默认为空格。
返回值
返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串
实例
以下实例展示了rjust()函数的使用方法：

str = "this is string example....wow!!!";
print str.rjust(50, '0');
以上实例输出结果如下：
000000000000000000this is string example....wow!!!

笔记2-Python bin() 函数

描述
bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
语法
以下是 bin() 方法的语法:
bin(x)
参数
x -- int 或者 long int 数字 
返回值
字符串。

实例
以下展示了使用 bin 函数的实例： 
>>>bin(10)
'0b1010'
>>> bin(20)
'0b10100'
'''
