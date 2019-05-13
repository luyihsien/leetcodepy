#https://www.cnblogs.com/zuoyuan/p/3701639.html
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    #self==hasCycle(head)
    def hasCycle(self, head):#hasCycle(head)被當self傳入使用同func()使用()內參數
        if head == None or head.next == None:#while if等等判別或非None or 0則為True
            return False
        slow = fast = head
        while fast and fast.next:#不是fast與slow 而是fast與fast.next 因為包含奇與偶#若fast為None while讀到fast即跳出故不會因fast.next不存在而error
            slow = slow.next#用來當作若是其實有cycle時候的辦別特徵
            fast = fast.next.next#已驗過原fast與fest.next非空#fast.next.next可能空可能有值
            if slow == fast:#fast倒追slow一圈#每次fast比slow多跑一格<誤>奇偶不會遇到
                return True
        return False#非while內，故跳出while會執行這一列#原本沒有符合的話就None，同函數性質

head=ListNode(5)
head.next(ListNode(4))
head.next(ListNode(3))
