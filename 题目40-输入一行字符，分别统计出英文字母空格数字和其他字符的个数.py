'''
题目描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
 
    /**
     * 统计出英文字母字符的个数。
     * 
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getEnglishCharCount(String str)
    {
        return 0;
    }
    
    /**
     * 统计出空格字符的个数。
     * 
     * @param str 需要输入的字符串
     * @return 空格的个数
     */
    public static int getBlankCharCount(String str)
    {
        return 0;
    }
    
    /**
     * 统计出数字字符的个数。
     * 
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getNumberCharCount(String str)
    {
        return 0;
    }
    
    /**
     * 统计出其它字符的个数。
     * 
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getOtherCharCount(String str)
    {
        return 0;
    }
 
 
输入描述:
输入一行字符串，可以有空格
输出描述:
统计其中英文字符，空格字符，数字字符，其他字符的个数
示例1 
输入
1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][

输出
26
3
10
12
'''
while True:
    try:
        s=input().strip()#去除首尾的空格
        n1,n2,n3,n4=0,0,0,0
        for e in s:
            if 'a'<=e<='z' or 'A'<=e<='Z':
                n1+=1
            elif e==' ':
                n2+=1
            elif '0'<=e<='9':
                n3+=1
            else:
                n4+=1
        print(n1,n2,n3,n4,sep='\n')
    except:
        break
