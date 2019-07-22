"""

题目标题： 
将两个整型数组按照升序合并，并且过滤掉重复数组元素[注: 题目更新了。输出之后有换行] 

输入描述:
输入说明，按下列顺序输入：
1 输入第一个数组的个数
2 输入第一个数组的数值
3 输入第二个数组的个数
4 输入第二个数组的数值
输出描述:
输出合并之后的数组

示例1 
输入
3
1 2 5
4
-1 0 3 2

输出
-101235
"""
while True:
    try:
        a,b,c,d=input(),list(map(int,input().split())),input(),list(map(int,input().split()))
        print("".join(map(str,sorted(list(set(b+d))))))
    except:
        break
