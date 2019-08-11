'''
import collections
c=collections.Counter(['a','b','c'])
print(c)
for i in c:
    print(c[i])
'''
class Solution:
    def minSwaps(self, data) -> int:
        count_one = sum(data)
        print('count_one',count_one)
        if count_one == 0:
            return 0

        n = len(data)
        cur = sum(data[:count_one])
        ans = cur
        print('ans',ans)
        for i in range(count_one, n):
            print('i',i,'n',n)
            print('data',data,'data[{}]'.format(i),data[i],'count_one',count_one,'data[{}]'.format(i-count_one),data[i - count_one])
            cur += data[i] - data[i - count_one]
            print('cur',cur)
            ans = max(ans, cur)
            print('ans',ans)

        return count_one - ans
#print(Solution().minSwaps([0,0,0,1,0]))
print(Solution().minSwaps([1,0,1,0,1,0,0,1,1,0,1]))