#https://www.cnblogs.com/zuoyuan/p/3701639.html
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #定在外面的變數可被class直接調用屬性，亦可被創造的物件使用A().a A.a
    #訂在__init__的variable只能被物件使用A().a
    # @param head, a ListNode
    # @return a boolean
    #self==Solution()<誤>self==hasCycle(head)
    def hasCycle(self, head):#hasCycle(head)被當self傳入同使用func()使用()內參數來做運算
        # 閉包函數內的內部函數可以使用外部函數的參數，內部函數使用內與外部函數參數運算完回傳值
        #函數or變數or class的object 都可看做object，都是被一自訂名字指向
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
#head.next(ListNode(3))#誤 這樣會複寫原本的head.next#即是將ListNode(4)變成ListNode(3)
