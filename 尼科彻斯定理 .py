"""
题目描述
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
例如：
1^3=1 
2^3=3+5 
3^3=7+9+11 
4^3=13+15+17+19 

 
输入描述:
输入一个int整数
输出描述:
输出分解后的string

示例1 
输入
6

输出
31+33+35+37+39+41
"""
while True:
    try:
        N = int(input())
        a = int(N ** 2 - N + 1)
        lst = [str(a)]#第一个奇数
        for i in range(1, N):
            lst.append(str(a + 2 * i))
        print('+'.join(lst))
    except:
        break
