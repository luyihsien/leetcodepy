#https://www.cnblogs.com/zuoyuan/p/3701639.html
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:#不是fast與slow 而是fast與fast.next 因為包含奇與偶#若fast為None while讀到fast即跳出故不會因fast.next不存在而error
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

head=ListNode(5)
head.next(ListNode(4))
head.next(ListNode(3))
