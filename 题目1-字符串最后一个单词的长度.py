'''
题目：
计算字符串最后一个单词的长度，单词以空格隔开。
输入：hello world   输出：5

题目分析：
输入一行：input()
输入的一行有多个信息：input().split()
'''
a=input().split()
print(len(a[-1]) if len(a)>1 else len(a[0]))
