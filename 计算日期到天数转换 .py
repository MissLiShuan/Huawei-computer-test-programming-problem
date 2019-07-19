"""
题目描述
根据输入的日期，计算是这一年的第几天。。
详细描述：
输入某年某月某日，判断这一天是这一年的第几天？。
 
 
接口设计及说明：
 /*****************************************************************************
 Description   : 数据转换
 Input Param   : year 输入年份
                Month 输入月份
                Day 输入天
                    
 Output Param  :
 Return Value  : 成功返回0，失败返回-1（如：数据错误）
 *****************************************************************************/
 public static int iConverDateToDay(int year, int month, int day)
 {
     /* 在这里实现功能，将结果填入输入数组中*/ 
     return 0;
 }
 
 /*****************************************************************************
 Description   : 
 Input Param   :
                    
 Output Param  :
 Return Value  : 成功:返回outDay输出计算后的第几天;
                                           失败:返回-1
 *****************************************************************************/
 public static int getOutDay()
 {
  return 0;
 }
 
 
 
 
输入描述:
输入三行，分别是年，月，日
输出描述:
成功:返回outDay输出计算后的第几天;
                                           失败:返回-1
示例1 
输入
2012
12
31
输出
366
"""
while True:
    try:
        [year, month, day] = [int(i) for i in input().split()]
        monthday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = sum(monthday[:month - 1]) + day
        if month > 2 and year % 4 == 0 or year % 400 == 0 and year % 100 != 0:#闰年判定方法：能被400整除。或者能被4整除但不能被100整除。
            days += 1
        print(days)
    except:
        break
