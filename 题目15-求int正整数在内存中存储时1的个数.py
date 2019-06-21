'''
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
 
输入描述:
输入一个整数（int类型）
 
输出描述:
这个数转换成2进制后，输出1的个数
 
示例1 
输入
5
输出
2
'''

num = bin(int(input()))
result=0
for i in range(2,len(num)):
    if int(num[i])==1:
        result +=1
print(result)
        

#笔记1###############Python中的数据转换####################################
'''
在python中可以通过内置方法进行相应的进制转换，但需记得转化成非十进制时，都会将数字转化成字符串

转化成二进制
a = 10  #声明数字，默认十进制
b = bin(a)
print(b , type(b))
运行结果：
<0b1010>
<class 'str'>

转化成八进制
a = 10  #声明数字，默认十进制
b = oct(a)
print(b , type(b))
运行结果：
<0c12>
<class 'str'>

转化成16进制
a = 10  #声明数字，默认十进制
b = hex(a)
print(b , type(b))
运行结果：
<0xa>
<class 'str'>

将非二进制数转化成十进制数
用int()方法可以将非十进制数转化成十进制，语法int(字符串数字，base=2\8\16(表示字符串数字本身是2进制还是8进制还是16进制))
a = '011'
print(int(a,base=2))
print(int(a,base=8))
print(int(a,base=16))
运行结果：
{{uploading-image-959842.png(uploading...)}}
