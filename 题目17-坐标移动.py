
'''
题目描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，
从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
 
输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
 
下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
 
处理过程： 
起点（0,0） 
+   A10   =  （-10,0） 
+   S20   =  (-10,-20) 
+   W10  =  (-10,-10) 
+   D30  =  (20,-10) 
+   x    =  无效 
+   A1A   =  无效 
+   B10A11   =  无效 
+  一个空 不影响 
+   A10  =  (10,-10) 
 
结果 （10， -10）

输入描述:
一行字符串

输出描述:
最终坐标，以,分隔

示例1 
输入
A10;S20;W10;D30;X;A1A;B10A11;;A10;

输出

10,-10
'''

while True:
    try:
        text = input().split(';')
        initx = 0
        inity = 0
        for i in text:
            if len(i) ==2:
                if i[0] == 'A' and 47<ord(i[1])<58:#47<ord(i[1])<58是数字[0,9]区间
                    initx -= int(i[1:])
                if i[0] == 'D' and 47<ord(i[1])<58:
                    initx += int(i[1:])
                if i[0] == 'W' and 47<ord(i[1])<58:
                    inity += int(i[1:])
                if i[0] == 'S' and 47<ord(i[1])<58:
                    inity -= int(i[1:])
            if len(i) ==3:
                if i[0] == 'A' and 47<ord(i[1])<58 and 47<ord(i[2])<58:
                    initx -= int(i[1:])
                if i[0] == 'D' and 47<ord(i[1])<58 and 47<ord(i[2])<58:
                    initx += int(i[1:])
                if i[0] == 'W' and 47<ord(i[1])<58 and 47<ord(i[2])<58:
                    inity += int(i[1:])
                if i[0] == 'S' and 47<ord(i[1])<58 and 47<ord(i[2])<58:
                    inity -= int(i[1:])
            else:
                continue
        print(str(initx) + ',' + str(inity))
    except:
        break
