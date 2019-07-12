"""
题目描述
输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。 
链表结点定义如下： 
struct ListNode 
{ 
int       m_nKey; 
ListNode* m_pNext; 
}; 
详细描述： 
接口说明 
原型： 
ListNode* FindKthToTail(ListNode* pListHead, unsignedint k); 
输入参数： 
ListNode* pListHead  单向链表 
unsigned int k  倒数第k个结点 
输出参数（指针指向的内存区域保证有效）： 
无 
返回值： 
正常返回倒数第k个结点指针，异常返回空指针 


输入描述:
输入说明
1 输入链表结点个数
2 输入链表的值
3 输入k的值
输出描述:
输出一个整数
示例1 
输入
8
1 2 3 4 5 6 7 8
4
输出
5
"""
while True:
    try:
        n = int(input())
        linkedT = list(map(int,input().split()))
        k = int(input())
        if k == 0:
            print (0)
        else:
            print(linkedT[-k])
    except:
        break
