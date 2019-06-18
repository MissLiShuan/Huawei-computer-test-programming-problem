'''
题目描述
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。 

输入描述:
输入一个有字母和数字以及空格组成的字符串，和一个字符。

输出描述:
输出输入字符串中含有该字符的个数。

示例1 
输入
ABCDEF A

输出
1
'''

a = input()
b = input()
print(a.lower().count(b.lower())) #lower() 转换字符串中所有大写字符为小写。
#笔记1 #####################count()的用法####################
'''
描述:count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

语法：str.count(sub, start= 0,end=len(string))

参数:
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

返回值
该方法返回子字符串在字符串中出现的次数。
实例
以下实例展示了count()方法的实例：
实例(Python 2.0+)
#!/usr/bin/python
 
str = "this is string example....wow!!!";
 
sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)
以上实例输出结果如下：
str.count(sub, 4, 40) :  2
str.count(sub) :  1
'''
