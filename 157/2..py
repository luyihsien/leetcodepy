import collections
class Solution:
    def longestSubsequence(self, arr, difference: int):
        d={arr[0]:1}
        n=len(arr)
        for i in range(1,n):
            if arr[i]-difference in d:
                d[arr[i]]=d[arr[i]-difference]+1
                print(i,d)
            elif arr[i] not in d:
                d[arr[i]]=1
        return max(d.values())
print(Solution().longestSubsequence(arr = [-1,1,3,5,7,9,5,7,9,11,13,1,3,5,7,9,11,13], difference = 2))
s = 'mississippi'
d = collections.defaultdict(int)
print(d)
class Solution(object):
    def longestSubsequence(self, A, D):
        count = collections.defaultdict(int)
        print('count',count)
        for x in A:
            #prev + d = x
            # prev = x-d
            print('count', count)
            count[x] = max(count[x], count[x-D] + 1)
        return max(count.values())
print(Solution().longestSubsequence([-1,1,3,5,7,9,5,7,9,11,13,1,3,5,7,9,11,13],2))
a=collections.defaultdict(list)
a['s']=1
print(a)