class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        #low=0#不可設0 因為其差其實不是賣-買的結果也並不是用low表示其差，而是最小買入點，若設為0，即什麼買入成本都不用，若數值全正數，跑出來的結果不可能正確
        #m=0
        #m=float('-inf')#應設為0不然負值全進去了
        low=prices[0]#low=float('inf')??
        low=float('inf')
        m=0#最糟是0
        for i in range(len(prices)):
            print('len(price)',len(prices))
            print('i第幾項',i)#0 1 2 3 4 5
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