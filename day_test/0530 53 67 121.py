class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        low=0
        #m=0
        m=float('-inf')
        for i in range(len(prices)):
            if prices[i]>low:
                low=prices[i]
                print(low)
            if m<prices[i]-low:
                m=prices[i]-low
                print(m)
        return m
print(Solution().maxProfit([7,1,5,3,6,4]))
'''
输入
[7,1,5,3,6,4]
输出
0
预期结果
5
'''