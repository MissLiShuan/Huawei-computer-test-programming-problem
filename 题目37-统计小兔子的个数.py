'''
题目描述
有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问每个月的兔子总数为多少？
 
    /**
     * 统计出兔子总数。
     * 
     * @param monthCount 第几个月
     * @return 兔子总数
     */
    public static int getTotalCount(int monthCount)
    {
        return 0;
    }
 
 
输入描述:
输入int型表示month
输出描述:
输出兔子总数int型

示例1 
输入
9

输出
34
'''
'''
思路分析：
关键是找到递推式 f(n)=f(n-1)+f(n-2) (n>=4)
递推式的解释:对于第n个月的兔子数量：有两部分组成，
一部分是上个月的兔子f(n-1)，另一部是满足3个月大的兔子
会生一只兔子f(n-2)
'''
while True:
    try:
        month = int(input())
        if month < 3:
            print(1)
        else:
            a, b = 1,1
            for i in range(3, month+1):
                a, b = b, a+b
            print(b)
    except:
        break
