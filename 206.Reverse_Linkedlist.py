#https://blog.csdn.net/coder_orz/article/details/51306170
#(head=head.next)!=(head.next=head)#自己指向自己!=自己變成下一個原本指向的對象


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        new_head = None
        while head:#到最後head都成None了(不是head.value歐，是整個已經不是ListNode而是None)，更遑論head.next<誤>有一個新new_head但原本的不變
            p = head
            head = head.next#要先跑去原本的next先存起來#然而是下次才供p new_head等等使用
            p.next = new_head
            new_head = p#上一顆None下一次的next
        return new_head# return p 可以嗎??