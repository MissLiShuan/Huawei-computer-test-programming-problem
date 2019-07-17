"""
题目描述
问题描述：给出4个1-10的数字，通过加减乘除，得到数字为24就算胜利
输入：
4个1-10的数字。[数字允许重复，但每个数字仅允许使用一次，测试用例保证无异常数字]
输出：
true or false 
输入描述:
输入4个int整数
输出描述:
返回能否得到24点，能输出true，不能输出false

示例1 
输入
7 2 1 10
输出
true
"""
def f(res,n):
    x = False
    if len(n) == 1:
        if n[0] ==res:
            return True
        else:
            return False
    for i in range(len(n)):
        a = n[i]
        b = n[:]
        b.remove(a)#除了n[i]之外，剩余的数据
        x = x or f(res-a,b) or f(res*a,b) or f(res/a,b) or f(res+a,b)
    return x
while True:
    try:
        n = input().split()
        flag = False
        if len(n) != 4:
            print('false')
            break
        for i in range(4):
            n[i] = float(n[i])
        if f(24.0, n):
            print('true')
        else:
            print('false')
    except:
        break
