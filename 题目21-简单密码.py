'''
题目描述
密码是我们生活中非常重要的东东，我们的那么一点不能说的秘密就全靠它了。
哇哈哈. 接下来渊子要在密码之上再加一套密码，虽然简单但也安全。  
假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，
他通过一种算法把这个密码变换成YUANzhi1987，这个密码是他的名字和出生年份，
怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。  
他是这么变换的，大家都知道手机上的字母： 
1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,
就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换， 
声明：密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，
如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。
 
输入描述:
输入包括多个测试数据。输入是一个明文，密码长度不超过100个字符，输入直到文件结尾
输出描述:
输出渊子真正的密文

示例1 
输入
YUANzhi1987

输出
zvbo9441987
'''

new = ""
while True:
 
    try:
        m=input()#输入密码字符串
 
        for i in m:#遍历字符串
            if i.isupper() :#如果字符是大写的
                if i is not 'Z':#如果字符是大写且不是Z,
                    new+=chr(ord(i.lower())+1)#则先将字符转换成小写，再转换成ASCII码，ASCII码+1，最后转换成字符，即先变成小写，再往后移一位。
                elif  i is 'Z':#如果字符是大写且是Z,
                    new+='a'#则将字符转换成a
            elif i.islower():#如果字符是小写的
                if i in 'abc':
                    new += '2'
                elif i in 'def':
                    new += '3'
                elif i in 'ghi':
                    new += '4'
                elif i in 'jkl':
                    new += '5'
                elif i in 'mno':
                    new += '6'
                elif i in 'pqrs':
                    new += '7'
                elif i in 'tuv':
                    new += '8'
                elif i in 'wxyz':
                    new += '9'
            elif i.isdigit():
                new+=i
 
    except:
        break
 
print(new.strip())

    
        

#笔记1###############isupper()####################################
'''
isdigit( )  检测字符串是否只由数字组成。  和 isnumeric( )函数类似
islower( )   检测字符串是否由小写字母组组成
isupper( )  检测字符串中所有的字母是否都为大写
isalpha( )  检测字符串是否只由字母组成
isspace( )  检测字符串是否只由空格组成

描述
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
语法：str.strip([chars]);
参数：chars -- 移除字符串头尾指定的字符序列。
返回值：返回移除字符串头尾指定的字符生成的新字符串。
实例：
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
str = "00000003210Runoob01230000000"; 
print str.strip( '0' );  # 去除首尾字符 0
 
 
str2 = "   Runoob      ";   # 去除首尾空格
print str2.strip();
以上实例输出结果如下：
3210Runoob0123
Runoob
从结果上看，可以注意到中间部分的字符并未删除。
以上下例演示了只要头尾包含有指定字符序列中的字符就删除：
实例
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
str = "123abcrunoob321"
print (str.strip( '12' ))  # 字符序列为 12
以上实例输出结果如下：
3abcrunoob3
'''
