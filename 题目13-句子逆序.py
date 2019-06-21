'''
题目描述
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符

接口说明
/**
 * 反转句子
 * 
 * @param sentence 原句子
 * @return 反转后的句子
 */
public String reverse(String sentence);
 
 
 
输入描述:
将一个英文语句以单词为单位逆序排放。

输出描述:
得到逆序的句子

示例1 
输入
I am a boy

输出
boy a am I
'''

str = input().split(' ')
ss=[]
for i in str[::-1]:
    ss.append(i)
print(' '.join(ss))

#笔记1###############join()####################################
'''
描述
join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
语法

str.join(sequence)
参数
sequence -- 要连接的元素序列。
返回值
返回通过指定字符连接序列中元素后生成的新字符串。
实例
以下实例展示了join()的使用方法：
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
以上实例输出结果如下：
a-b-c

'''
