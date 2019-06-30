'''
题目描述
1、对输入的字符串进行加解密，并输出。
2加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
3、解密方法为加密的逆过程。
 
接口描述：
    实现接口，每个接口实现1个基本操作：
void Encrypt (char aucPassword[], char aucResult[])：在该函数中实现字符串加密并输出
说明：
1、字符串以\0结尾。
2、字符串最长100个字符。
 
int unEncrypt (char result[], char password[])：在该函数中实现字符串解密并输出
说明：
1、字符串以\0结尾。
    2、字符串最长100个字符。
 
 
 
输入描述:
输入一串要加密的密码
输入一串加过密的密码

输出描述:
输出加密后的字符
输出解密后的字符

示例1 
输入
abcdefg
BCDEFGH
输出
BCDEFGH
abcdefg
'''
while True:
    try:
        a=input()#输入一串要加密的密码
        b=input()#输入一串加过密的密码
        aa=""
        bb=""
        for i in a:#遍历一串要加密的密码
            if i.islower():#如果是小写的字母
                if i != "z":#如果不是z
                    aa+=chr(ord(i)+1).upper()#则先将i的ASCII码加1，然后转换成大写
                else:
                    aa+="A"#如果是z，则输出是A
            elif i.isupper():#如果不是小写字母而是大写字母
                if i!="Z":#如果不是Z
                    aa+=chr(ord(i)+1).lower()#则先将i的ASCII码加1，然后转换成小写
                else:
                    aa+="a"#如果是z，则输出是a
            elif i.isdigit():#如果是数字
                if i!="9":#如果不是9
                    aa+=chr(ord(i)+1)#则将i的ASCII码加1
                else:
                    aa+="0"#如果是9，则转换成0
        for i in b:#解码的思路同上，不过是减1
            if i.islower():
                if i!="a":
                    bb+=chr(ord(i)-1).upper()
                else:
                    bb+="Z"
            elif i.isupper():
                if i!="A":
                    bb+=chr(ord(i)-1).lower()
                else:
                    bb+="z"
            elif i.isdigit():
                if i !="0":
                    bb+=chr(ord(i)-1)
                else:
                    bb+="9"
        print(aa)
        print(bb)
    except:
        break
