# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#思路:先把Linked_list倒過來再逐數相加#法二:先放至空List，放完後revese再弄Linkedlist
class Solution:
    def addTwoNumbers(self, l1, l2):#l1 l2不像List是直接一串，它只保留value以及下一項指向的東東
        new_head1=None
        while l1:
            p=l1
            l1=l1.next
            p.next=new_head1
            new_head1=p
            #return new_head1
        new_head2=None
        while l2:#若為空就直接跳出了
            p=l2#why不直接改l2??#因為改了就沒有人幫跑下一個原本的node
            l2=l2.next#不是只有值而已而是整顆Node
            p.next=new_head2#p是已完成反轉的None，暫時存起#不是p=new_head
            new_head2=p
        #Q:1.Linked list的len是否相同2.倒過來以後0會不會有影響
        while new_head2
            #return new_head2


        '''
        for i in range(flag1):
            a=a+(10**i)*(new_head1.value)
            new_head1=new_head1.next
        for i in range(flag2):
            b=b+(10**i)*(new_head2.value)
            new_head2=new_head2.next
        return a+b
        '''







