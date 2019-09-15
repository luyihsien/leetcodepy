'''
822. Reverse Order Storage
中文English
Give a linked list, and store the values of linked list in reverse order into an array.

样例
Example1

Input: 1 -> 2 -> 3 -> null
Output: [3,2,1]
Example2

Input: 4 -> 2 -> 1 -> null
Output: [1,2,4]
注意事项
You can not change the structure of the original linked list.
ListNode have two elements: ListNode.val and ListNode.next
'''

#Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

l=[]
m=[]
class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order 
    """
    def reverseStore(self, head):
        if head==None:
            return None
        while head!=None:
            l.append(head.val)
            head=head.next
        l.reverse()
        for i in range(len(l)-1):
            n=ListNode(l[i])
            n.next=ListNode(l[i+1])
            m.append(n)
        e=ListNode(l[-1])
        m.append(e)
        return m


class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order 
    """

    def reverseStore(self, head):
        # write your code here
        ans = []
        self.helper(head, ans)
        return ans

    def helper(self, head, ans):
        if head is None:
            print('沒有回傳')
            return
        else:
            self.helper(head.next, ans)
        ans.append(head.val)
        print(ans)
a=ListNode(5)
a.next=ListNode(3)
a.next.next=ListNode(4)
Solution().reverseStore(a)