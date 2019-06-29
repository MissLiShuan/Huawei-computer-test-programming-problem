'''
题目描述
实现一个可存储若干个单词的字典，用户可以：
在字典中加入单词。
查找指定单词在字典中的兄弟单词个数。
查找指定单词的指定序号的兄弟单词，指定序号指字典中兄弟单词按字典顺序排序后的序号
清空字典中所有单词

定义，格式说明
单词：由小写英文字母组成，不含其他字符
兄弟单词：给定一个单词X，如果通过任意交换单词中字母的位置得不到的单词Y，
        那么定义Y是X的兄弟单词。
字典顺序：
    两个单词（字典按照自左向右顺序），先以第一个字母作为排序的基准，如果第一个字母相同，
    就用第二个字母为基准，如果第二个字母相同就以第三个字母为基准，依次类推，
    如果到某个字母不相同，字母顺序在前的那个单词顺序在前，如果短单词是长单词
    从首字母开始连续的一部分，短单词顺序在前。
    
举例：bca是abc的兄弟单词；
    abc与abc是相同单词，不是兄弟单词。
输入描述:
先输入字典中单词的个数，再输入n个单词作为字典单词。
输入一个单词，查找其在字典中兄弟单词的个数
再输入数字n
输出描述:
根据输入，输出查找到的兄弟单词的个数

规格
0 <= 字典中所含单词个数 <= 1000
1 <= 单词所含字母数   <= 50

示例1 
输入
3	abc	bca	cab	abc	1

输出
2	bca

'''
while True:
    try:
        s = input().strip().split()#strip()删除开头结尾的空格，split()以空格将输入隔开
        num = int(s[0])# 取字符串的首部
        bro_search_num = int(s[-1])#取字符串的尾部
        word_list = []#存放单词列表
        for i in range(1, num+1):
            word_list.append(s[i])
        bro_search_word = s[i+1]#保存需要查找兄弟单词的单词
 
        result = []
        for word in word_list:#遍历单词列表
            if word==bro_search_word or len(word)!=len(bro_search_word):#如果单词和要查找兄弟单词的单词相同或则单词的长度不等于要查找兄弟单词的单词
                continue#则跳过该循环
            #查找单词
            letter = list(word)
            for l in bro_search_word:#
                if l in letter:
                    letter.remove(l)
            if len(letter) == 0:
                result.append(word)
 
        result.sort()
        print(len(result))
        if bro_search_num <= len(result):
            print(result[bro_search_num-1])
 
    except:
        break
