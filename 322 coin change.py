
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [0 for _ in range(amount + 1)]

        for i in range(1, amount + 1):
            print('i',i)
            cost = float('inf')
            for c in coins:#[2]
                print('i-c',i-c)
                if i - c >= 0:
                    cost = min(cost, res[i - c] + 1)
                print('res',res)
            res[i] = cost
            print('res final',res)

        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]
print(Solution().coinChange([2],3))
print(Solution().coinChange([1,2,5],11))
print(Solution().coinChange([2,5],11))

'''
作者：jalan
链接：https: // leetcode - cn.com / problems / two - sum / solution / dong - tai - gui - hua - python - ti - jie - by - jalan - 3 /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
print(min(float('inf'),float('inf')-float('inf')-1000000))#無限大減無限大還是無限大