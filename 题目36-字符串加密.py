'''
题目描述
有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。下面是它的工作原理：
首先，选择一个单词作为密匙，如TRAILBLAZERS。如果单词中包含有重复的字母，只保留第1个，
其余几个丢弃。现在，修改过的那个单词属于字母表的下面，如下所示： 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
T R A I L B Z E S C D F G H J K M N O P Q U V W X Y 
上面其他用字母表中剩余的字母填充完整。在对信息进行加密时，信息中的每个字母被固定于顶上那行，
并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该保留)。因此，
使用这个密匙，Attack AT DAWN(黎明时攻击)就会被加密为Tpptad TP ITVH。 
请实现下述接口，通过指定的密匙和明文得到密文。 
详细描述： 
接口说明 
原型： 
voidencrypt(char * key,char * data,char * encrypt); 
输入参数： 
char * key：密匙 
char * data：明文 

输出参数： 
char * encrypt：密文 

返回值： 
void 


输入描述:
先输入key和要加密的字符串

输出描述:
返回加密后的字符串

示例1 
输入
nihao
ni

输出
le
'''
while True:
    try:
 
        def encryption(s):#s[0]是密钥,s[1]是要加密的字符串
            encryl = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']#存放26个字母
            encryd = []
            index = []
            for i in range(len(s[0])):#遍历密钥
                if (s[0][i].lower() not in encryd) and (s[0][i].upper() not in encryd):#如果密钥的字母大小写都不在encryd
                    encryd.append(s[0][i])#则添加到encryd即，不重复的将密钥放入到encryd中
            for j in encryl:#遍历字母表
                if (j.lower() not in encryd) and (j.upper() not in encryd):#如果字母表的大小写都不在encryd中
                    encryd.append(j)#则添加到encryd中
                else:
                    continue
            #以上俩循环实现了将密钥去重放入到encryd中，再将存在于字母表中却不存在于密钥中的字母放入到encryd中
            for k in range(len(s[1])):#遍历要加密的字符串
                for x in range(len(encryl)):#遍历变换后的密钥，即encryd
                    if s[1][k] == encryl[x].lower() or s[1][k] == encryl[x].upper():#如果要加密的字母等于encryd中字母的大写或小写
                        index.append(x)#则存放入到index中，该步是找到，要加密的字符串的字母在字母表中的索引
                    else:
                        continue
            nencry = ''
            for i in range(len(index)):#遍历index
                if s[1][i].islower():#如果要加密的字符是小写字母
                    nencry += encryd[index[i]].lower()#从密钥中找到index位置的字母，返回该字母的小写
                if s[1][i].isupper():#如果要加密的字符是大写字母
                    nencry += encryd[index[i]].upper()#从密钥中找到index位置的字母，返回该字母的大写
            print(nencry)
        s = []
        for i in range(2):
            s.append(input())
        encryption(s)
    except:
        break
