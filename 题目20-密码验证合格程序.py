'''
题目描述
密码要求: 
1.长度超过8位 
2.包括大小写字母.数字.其它符号,以上四种至少三种 
3.不能有相同长度超2的子串重复
说明:长度超过2的子串

输入描述:
一组或多组长度超过2的子符串。每组占一行
输出描述:
如果符合要求输出：OK，否则输出NG

示例1 
输入
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000

输出
OK
NG
NG
OK

'''

def fun1(s):
    if len(s)>8:
        return True
    else:
        return False
  
def fun2(s):
    num1=0
    num2=0
    num3=0
    num4=0
    for ss in s:
        if 'a'<=ss<='z' :
            num1=1
        elif 'A'<=ss<='Z':
            num2=1
        elif '1'<=ss<='9':
            num3=1
        else:
            num4=1
    if (num1+num2+num3+num4)>=3:
        return True
    else:
        return False
  
def fun3(s):
    for i in range((len(s)-3)):
         if s[i:i+3] in s[i+1:]:
             return False
             break
    return True
  
while True:
    try:
        a=input()
        if fun1(a) and fun2(a) and fun3(a):
            print('OK')
        else:
            print('NG')
    except:
           break
