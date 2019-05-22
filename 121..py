class Solution:
    def maxProfit(self, prices):
        s=0
        m=0
        #sum=0#要加還是不加??
        for i in prices:
            for j in prices[i:len(prices)-1]:
                sum=prices[i]-prices[j]#Index error:List index out of range#s[i]-s[j] is error
                if sum>=0 and sum>m:
                    m=sum
        return m
'''
TypeError: 'int' object is not subscriptable
Line 8 in maxProfit (Solution.py)
'''
a=[1,2,3]
#print(a.pop().pop())#Error:int object has no attribute 'pop'
#print(a.remove(1).remove(2))#AttributeError: 'NoneType' object has no attribute 'remove'
#print(a.remove(3))#None
#a.remove(3)
#print(a)
#print(a.pop())
#print(a)

print(a)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        opt = [0] * len(prices)
        for i in range(1, len(prices)):
            opt[i] = max(opt[i-1]+prices[i]-prices[i-1], 0)
            print(opt)
        return max(opt)
Solution().maxProfit([10,3,2,6,9,7,1,2,5,2,0,9,7,100])