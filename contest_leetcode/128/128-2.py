import collections

class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        n = len(time)
        d = {}
        a = 0
        for i in range(n):
            time[i] = time[i] % 60#i寫成n
            #d[time[i]] = 0
            #print('d',d)
            if (60 - time[i])%60 in d:
                d[(60 - time[i])%60] += 1
            if time[i] not in d:
                d[time[i]] =0
                #print('d',d)
        for i in d:
            a+=d[i]
                #print(d)
        return a
#print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))#Line 7: IndexError: list index out of range
print(Solution().numPairsDivisibleBy60([418,204,77,278,239,457,284,263,372,279,476,416,360,18]))
print(Solution().numPairsDivisibleBy60([60,60,60]))
print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))
#[418,204,77,278,239,457,284,263,372,279,476,416,360,18]
#c=Counter('hello')
#print(c)
#默認請求下，訪問不存在的 item，會返回 0。Counter 可以用來統計某些數據的出現次數，比如一個很長的數字串 numbers = "67642192097348921647512014651027586741512651" 中每個數字的頻率：

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        memo = collections.Counter()
        res = 0
        for t in time:
            print('memo',memo)
            print('t',t)
            t %= 60
            print('t %= 60後',t)
            res += memo[(60-t)%60]#讓60-0 60-60都一樣
            print('memo',memo)
            print('memo[(60-t)%60]=memo[{}]='.format((60-t)%60),memo[(60-t)%60])
            print('res',res)
            memo[t] += 1
            print('memo[t]',memo[t],'memo',memo)
        return res
Solution().numPairsDivisibleBy60([418,204,77,278,239,457,284,263,372,279,476,416,360,18])
print(Solution().numPairsDivisibleBy60([60,60,60,60]))
print(Solution().numPairsDivisibleBy60([1,59,23,37]))

class Solution:#[30,20,150,100,40]輸出4 應為3#[30,20,30,40,40]
    def numPairsDivisibleBy60(self, time) -> int:
        n = len(time)
        d = {}
        a = 0
        for i in range(n):
            time[i] = time[i] % 60#i寫成n
            #d[time[i]] = 0
            #print('d',d)
            if time[i] not in d:
                d[time[i]] =0
            if (60 - time[i])%60 in d:
                d[(60 - time[i])%60] += 1
                #print('d',d)
            print('d',d)
        for i in d:
            a+=d[i]
                #print(d)
        return a
print(Solution().numPairsDivisibleBy60([30,20,30,40,40]))
