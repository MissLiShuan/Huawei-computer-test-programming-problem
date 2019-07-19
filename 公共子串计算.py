"""
题目标题：
计算两个字符串的最大公共字串的长度，字符不区分大小写
详细描述：
接口说明
原型：
int getCommonStrLength(char * pFirstStr, char * pSecondStr);
输入参数：
     char * pFirstStr //第一个字符串
     char * pSecondStr//第二个字符串
 
输入描述:
输入两个字符串
输出描述:
输出一个整数

示例1 
输入
asdfas werasdfaswer
输出
6
"""
while True:
    try:
        a = str(input())
        b = str(input())
        n = 0
        for i in range(len(a)):
            if a[i-n:i+1] in b:
                n += 1
        print(n)
    except:
        break
