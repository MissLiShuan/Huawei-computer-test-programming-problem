"""
题目描述
如果A是个x行y列的矩阵，B是个y行z列的矩阵，把A和B相乘，
其结果将是另一个x行z列的矩阵C。这个矩阵的每个元素是由下面的公式决定的： 
 
原型：
voidmatrix_multiply(int *m1,int *m2,int *r, int x, int y, int z);
输入参数：
    int *m1：x行y列的矩阵(array1[x][y])
    int *m2：y行z列的矩阵(array2[y][z])
    int x：矩阵m1的行数
    int y：矩阵m1的列数/矩阵m2的行数
    int z：矩阵m2的列数
 
输出参数：
    int *r：矩阵m1, m2相乘的结果(array3[x][z])
 
返回值：
        void
 
 
输入描述:
输入说明：
1、第一个矩阵的行数
2、第一个矩阵的列数和第二个矩阵的行数
3、第二个矩阵的列数
4、第一个矩阵的值
5、第二个矩阵的值
输出描述:
输出两个矩阵相乘的结果

示例1 
输入
2
2
2
3 8
8 0
9 0
18 9
输出
171 72
72 0
"""
while True: 
    try:
        x = int(input())#输入第一个矩阵的行数
        y = int(input())#第一个矩阵的列数和第二个矩阵的行数
        z = int(input())#第二个矩阵的列数 
        res = [[0 for i in range(z)] for j in range(x)]#初始化结果矩阵res为z*x        
        m1 = []        
        for i in range(x):#遍历第一个矩阵的行数            
            m1.append(list(map(int,input().split())))#该循环输入矩阵1的值        
        m2 = []        
        for i in range(y):#遍历第二个矩阵的行数                
            m2.append(list(map(int,input().split())))#该循环输入矩阵2的值          
        for i in range(x):#结果矩阵的行列为x*z            
            for j in range(z):                
                he = 0 #he表示结果矩阵中的第i行，第j列的值               
                for k in range(y):                    
                    he+=m1[i][k]*m2[k][j] #res[i,j]=矩阵1的行和矩阵2的列相乘，再相加的结果              
                res[i][j]=he        
        for i in res:            
            print(' '.join(map(str,i)))
                    
    except:    
        break
