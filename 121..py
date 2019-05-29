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
#a=[1,2,3]
#print(a.pop().pop())#Error:int object has no attribute 'pop'
#print(a.remove(1).remove(2))#AttributeError: 'NoneType' object has no attribute 'remove'
#print(a.remove(3))#None
#a.remove(3)
#print(a)
#print(a.pop())
#print(a)

#print(a)
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
print(Solution().maxProfit([10,3,2,6,9,7,1,2,5,2,0,9,7,100]))
#二刷 0529
class Solution:
    def maxProfit(self, prices):
        a=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if j-i>a:
                    print(j-i)
                    a=j-i
        return a
class Solution:
    def maxProfit(self, prices):
        a=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                #if j-i>a:
                if prices[j]-prices[i]>a:
                    a=prices[j]-prices[i]
        return a
print(Solution().maxProfit([7,1,5,3,6,4]))
#https://www.cnblogs.com/zuoyuan/p/3765934.html
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1: return 0
        low = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < low: low = prices[i]
            maxprofit = max(maxprofit, prices[i] - low)
        return maxprofit