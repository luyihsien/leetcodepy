class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        n = len(time)
        d = {}
        a = 0
        for i in range(n):
            time[n] = time[n] % 60
            if 60 - time[n] not in d:
                d[time[n]] = 0
                print(d)
            else:
                d[60 - time[n]] += 1
                print(d)
        for i in d:
            a += d[i]
            print(a)

        return a
Solution().numPairsDivisibleBy60([30,20,150,100,40])#Line 7: IndexError: list index out of range