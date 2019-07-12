"""
题目描述
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。
许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。
编辑距离的算法是首先由俄国科学家Levenshtein提出的，故又叫Levenshtein Distance。
Ex：
字符串A:abcdefg
字符串B: abcdef
通过增加或是删掉字符”g”的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。
要求：
给定任意两个字符串，写出一个算法计算它们的编辑距离。
  
请实现如下接口 
/*  功能：计算两个字符串的距离 
 *  输入： 字符串A和字符串B 
 *  输出：无 
 *  返回：如果成功计算出字符串的距离，否则返回-1 
 */ 
     public   static   int  calStringDistance (String charA, String  charB) 
    { 
        return  0; 
    }   
 

输入描述:
输入两个字符串
输出描述:
得到计算结果
示例1 
输入
abcdefg
abcdef
输出
1
"""

def editDistance(str1, str2):
    len1, len2 = len(str1) + 1, len(str2) + 1
    dp = [[0 for i in range(len2)] for j in range(len1)]#生成len1行len2列的 0 矩阵
    for i in range(len1):
        dp[i][0] = i
    for j in range(len2):
        dp[0][j] = j
    for i in range(1, len1):
        for j in range(1, len2):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]))
    return dp[-1][-1]
  
while True:
    try:
        print(editDistance(input(), input()))
    except:
        break

"""
* 字符串之间的距离，编辑距离，将strA编辑成strB所需的最小代价
 *编辑操作包括插入一个字符、删除一个字符、替换一个字符
 * 分别对应的代价是ic、dc、rc，insert cost、delete cost、replace cost
 * strA[x-1]代表strA的第x个字符，注意下标是从0开始的,strA[y-1]代表strA的第y个字符
 * 定义一个代价矩阵为(N+1)*(M+1)，M N 表示strA strB的长度
 * dp[x][y]表示strA的前x个字符串编辑成 strB的前y个字符所花费的代价
 * dp[x][y]是下面几种值的最小值：
     * 1、dp[x][y] = dp[x-1][y] + dc
     * dp[x-1][y]将strA的前x-1个字符编辑成strB的前y个字符的代价已知，
     * 那么将将strA的前x个字符编辑成strB的前y个字符的代价dp[x][y]就是dp[x-1][y] + dc
     * 相当于strA的前x-1个字符编辑成strB的前y个字符，现在变成了strA的前x个字符，增加了一个字符，要加上删除代价
     * 2、dp[x][y] = dp[x][y-1] + ic
     * dp[x][y-1]将strA的前x个字符编辑成strB的前y-1个字符的代价已知，
     * 现在变为strB的前y个字符，相应的在strA前x个操作代价的基础上插入一个字符
     * 3、dp[x][y] = dp[x-1][y-1]
     * dp[x-1][y-1]将strA的前x-1个字符编辑成strB的前y-1个字符的代价已知，
     * strA的第x个字符和strB的第y个字符相同，strA[x-1] == strB[y-1]，没有引入操作
     * 4、dp[x][y] = dp[x-1][y-1] + rc
     * strA的第x个字符和strB的第y个字符不相同，strA[x-1] ！= strB[y-1]，
     * 在strA的前x-1个字符编辑成strB的前y-1个字符的代价已知的情况下，
     * 计算在strA的前x字符编辑成strB的前y个字符的代价需要加上替换一个字符的代价
"""
