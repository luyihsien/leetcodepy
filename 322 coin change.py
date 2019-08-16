class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [0 for _ in range(amount + 1)]

        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i - c] + 1)
            res[i] = cost

        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]

'''
作者：jalan
链接：https: // leetcode - cn.com / problems / two - sum / solution / dong - tai - gui - hua - python - ti - jie - by - jalan - 3 /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''