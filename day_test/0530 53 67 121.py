class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        #low=0#不可設0 因為其差其實不是賣-買的結果
        #m=0
        #m=float('-inf')#應設為0不然負值全進去了
        for i in range(len(prices)):
            print(len(prices))
            print(i)#0 1 2 3 4 5
            #if prices[i]>low:#最小的給low
            if prices[i]<low:
                low=prices[i]
                print('low',low)
            if m<prices[i]-low:#m至少要在for此列以上or def與for之間放入，不可直接訂一個沒用過的m
                m=prices[i]-low
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