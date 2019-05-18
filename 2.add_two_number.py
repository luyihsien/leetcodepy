# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#思路:先把Linked_list倒過來再逐數相加
class Solution:
    def addTwoNumbers(self, l1, l2):
        l1.next=l1
