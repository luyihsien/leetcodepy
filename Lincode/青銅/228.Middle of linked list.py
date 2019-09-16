'''
228. Middle of Linked List
中文English
Find the middle node of a linked list.

样例
Example 1:

Input:  1->2->3
Output: 2	
Explanation: return the value of the middle node.
Example 2:

Input:  1->2
Output: 1	
Explanation: If the length of list is  even return the value of center left one.	
挑战
If the linked list is in a data stream, can you find the middle without iterating the linked list again?
'''
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head,l=[]):
        h=head
        while h:
            l.append(head.val)
            h=h.next
        n=len(l)
        while n-1:
            head=head.next
        return head


        # write your code here