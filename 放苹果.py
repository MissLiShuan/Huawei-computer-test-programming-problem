"""
题目描述
题目描述 
把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。 

输入 
每个用例包含二个整数M和N。0<=m<=10，1<=n<=10。 

样例输入 
7 3 

样例输出 
8 

/** 
* 计算放苹果方法数目 

* 输入值非法时返回-1 
* 1 <= m,n <= 10 
* @param m 苹果数目 
* @param n 盘子数目数 
* @return 放置方法总数 
* 
*/ 
public static int count(int m, int n) 



输入描述:
输入两个int整数
输出描述:
输出结果，int型
示例1 
输入
7 3

输出
8
题目分析：
放苹果分为两种情况，一种是有盘子为空，一种是每个盘子上都有苹果。 
令(m,n)表示将m个苹果放入n个盘子中的摆放方法总数。 
1.假设有一个盘子为空，则(m,n)问题转化为将m个苹果放在n-1个盘子上，即求得(m,n-1)即可 
2.假设所有盘子都装有苹果，则每个盘子上至少有一个苹果，即最多剩下m-n个苹果，问题转化为将m-n个苹果放到n个盘子上 
即求(m-n，n) 

"""

import sys
 
def f(m,n):
    if m < 0 or n < 0:
        return 0
    elif m ==1 or n == 1:
        return 1
    else:
        return f(m,n-1)+f(m-n,n)
while True:
    line1 = sys.stdin.readline().strip()#strip用于去除字符串首尾的字符，默认是空格、\n、\t
    if line1 == '':
        break
    line2 = line1.split(' ')
    m,n = map(int,line2)
    print(f(m,n))

"""
sys.stdin.readline()方法会获取每行数据的最后的换行符
"""
