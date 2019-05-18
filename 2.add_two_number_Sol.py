#解答:https://xiaozhuanlan.com/topic/4720839156
#搭配 join函數 http://www.runoob.com/python3/python3-string-join.html
#a=123
#print(reversed(123))#'int' object is not reversible
#print(123.reversed())#SyntaxError: invalid syntax 為什麼明明line 4是錯的還會執行到此列
#number沒有可以內建反轉的function不然也不會出成Leetcode easy了
'''
a=1000
b=1000
print(a is b)#True
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 获得 l1 和 l2 的 integer 表示
        val1, val2 = [l1.val], [l2.val]

        while l1.next:
            val1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            val2.append(l2.next.val)
            l2 = l2.next

        # 求出 l1 和 l2 代表的数字
        num1 = ''.join([str(i) for i in val1[::-1]])#將[str(i)...]值傳入 list->str
        num2 = ''.join([str(i) for i in val2[::-1]])

        # 得到 l1 和 l2 相加之和
        sums = int(num1) + int(num2)

        # 将 sums 转成题目中 linkedlist 所对应的表示形式
        sums = str(sums)[::-1]#沒有函數可以直接將數字倒序，故先化為str

        # dummy 作为返回结果#指標值與naxt 交給head來跑 而a=100000000 b=100000000 a is b  True故不只值相同記憶體也同#當包成ListNode也會同，but跟此處可能不太一樣狀況
        dummy = head = ListNode(int(sums[0]))
        for i in range(1, len(sums)):
        #for i in sums:
            head.next = ListNode(int(sums[i]))
            #ListNode(int(sums))
            head = head.next
        return dummy