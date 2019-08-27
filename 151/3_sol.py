
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def to_list(h):
    ans = []
    while h:
        ans.append(h.val)
        h = h.next
    return ans


def to_link(l):
    n = ListNode(None)
    h = n
    for node in l:
        n.next = ListNode(node)
        n = n.next
    return h.next


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = to_list(head)
        print(l)
        ans = list()
        for n in l:
            ans.append(n)
            s = 0
            for k in reversed(range(len(ans))):
                s += ans[k]
                if s == 0:
                    ans = ans[:k]
                    print('ans',ans)
                    break
            print(ans)
        return to_link(ans)
b=ListNode(0)
a=ListNode(1)
b.next=a
a.next=ListNode(2)
a.next.next=ListNode(-3)
a.next.next.next=ListNode(3)
a.next.next.next.next=ListNode(-2)
a.next.next.next.next.next=ListNode(2)
a.next.next.next.next.next.next=ListNode(1)

Solution().removeZeroSumSublists(b)