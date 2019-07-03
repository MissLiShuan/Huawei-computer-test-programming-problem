'''
题目描述
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？ 
 
    /**
     * 统计出第5次落地时，共经过多少米?
     * 
     * @param high 球的起始高度
     * @return 英文字母的个数
     */
    public static double getJourney(int high)
    {
        return 0;
    }
    
    /**
     * 统计出第5次反弹多高?
     * 
     * @param high 球的起始高度
     * @return 空格的个数
     */
    public static double getTenthHigh(int high)
    {
        return 0;
    }
 
 
输入描述:
输入起始高度，int型
输出描述:
分别输出第5次落地时，共经过多少米第5次反弹多高

示例1 
输入
1

输出
2.875
0.03125
'''
while True:
    try:
        h = int(input())
        num = 5
        distance = h + h + 0.5*h + 0.5**2*h + 0.5**3*h
        h5 = (0.5**5)*h
        print('%g'%distance)
        print('%g'%h5)
    except:
        break
