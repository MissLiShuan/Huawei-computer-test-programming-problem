'''
题目描述
编写一个程序，将输入字符串中的字符按如下规则排序。 
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。 
       如，输入： Type   输出： epTy 
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。 
     如，输入： BabA   输出： aABb 
规则 3 ：非英文字母的其它字符保持原来的位置。 
     如，输入： By?e   输出： Be?y 
样例： 
    输入： 
   A Famous Saying: Much Ado About Nothing(2012/8). 
    输出： 
   A  aaAAbc   dFgghh :  iimM   nNn   oooos   Sttuuuy  (2012/8). 

输入描述:
输出描述:

示例1 
输入
A Famous Saying: Much Ado About Nothing (2012/8).

输出
A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).

'''
while True:
    try:
        str=input()
        char=[]#存放字母
        res=[False]*len(str)#先使用False进行占位
        for i,v in enumerate(str):
            if v.isalpha():#如果是字母
                char.append(v)#放入到char
            else:#否则
                res[i]=v#不改变位置
        char.sort(key=lambda c:c.lower())#转换成小写字母，并按照小写字母的顺序排序
        for i,v in enumerate(res):#遍历res
            if not v:#如果是False
                res[i]=char[0]#将字母列表char中的元素从第一个开始取删，放入到res中
                char.pop(0)#然后从第一个元素开始删除char
        print(''.join(res))
    except:
        break
#笔记1###############join()方法####################################
'''
Python3 join()方法
描述
Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
语法
join()方法语法：
str.join(sequence)
参数
sequence -- 要连接的元素序列。
返回值
返回通过指定字符连接序列中元素后生成的新字符串。
实例
以下实例展示了join()的使用方法：
实例
#!/usr/bin/python3

s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
以上实例输出结果如下：
r-u-n-o-o-b
runoob
'''
