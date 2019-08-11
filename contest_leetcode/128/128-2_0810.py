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
print(Solution().numPairsDivisibleBy60([60,60,60,60]))
class Solution:#[60,60,60]錯誤#輸出2#預期3
    def numPairsDivisibleBy60(self, time) -> int:
        n = len(time)
        d = {}
        a = 0
        for i in range(n):
            time[i] = time[i] % 60#i寫成n
            #d[time[i]] = 0
            print('d',d)
            if (60 - time[i])%60 in d:
                d[(60 - time[i])%60] += 1
            if time[i] not in d:
                d[time[i]] =0
                #print('d',d)
        for i in d:
            a+=d[i]
                #print(d)
        return a

print(Solution().numPairsDivisibleBy60([60,60,60]))
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
            print('d',d)
        for i in d:
            a+=(d[i]*d[i]+1)//2

                #print(d)
        return a
print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))#[30,20,30,40,40]


class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        d = {}
        for i in range(len(time)):
            time[i] = time[i] % 60
            d[time[i]] = 0
            d[60 - time[i] % 60] = 0
        res = 0
        for i in time:
            res += d[(60 - i) % 60]
            d[i] += 1
        return res
