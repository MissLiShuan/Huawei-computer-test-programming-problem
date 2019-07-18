"""
题目描述
矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：
    A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵 
计算A*B*C有两种顺序：（（AB）C）或者（A（BC）），前者需要计算15000次乘法，后者只需要3500次。 
编写程序计算不同的计算顺序需要进行的乘法次数
  
输入描述:
输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则
输出描述:
输出需要进行的乘法次数
示例1 
输入
3
50 10
10 20
20 5
(A(BC))
输出
3500
"""
while True:
    try:
        n=int(input())#输入要计算乘法的矩阵个数
        arr=[]
        stack=[]#初始化一个空栈
        result=0
        for i in range(n):#遍历n,分别输入每个矩阵的行列数
            arr.append(list(map(int,input().split())))#将每个矩阵的行列数转换成int
        p=input()#输入要计算的法则
        for i in range(3*n-2):
            if p[i]=='(':
                pass
            elif p[i]==')':
                a=stack.pop()
                b=stack.pop()
                result=result+b[1]*a[1]*b[0]
                stack.append([b[0],a[1]])
            else:
                stack.append(arr[ord(p[i])-65])#ord()返回对应的 ASCII 数值,chr(65)为A
        print(result)
    except:
        break
