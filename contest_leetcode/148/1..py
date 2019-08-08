class Solution:
    def movesToMakeZigzag(self, nums: 'List[int]') -> int:
        n=len(nums)
        m1,m2=0,0
        a=[float('inf')]+nums+[float('inf')]
        print('a',a)
        for i in range(1,n,2):
            print('a[i]+1', a[i] + 1, 'min(a[i-1],a[i+1])', min(a[i - 1], a[i + 1]))
            m1+=max(0,a[i]+1-(min(a[i-1],a[i+1])))
            print('m1',m1)
        for i in range(2,n,2):
            print('a[i]+1', a[i] + 1, 'min(a[i-1],a[i+1])', min(a[i - 1], a[i + 1]))
            m2+=max(0,a[i]+1-(min(a[i-1],a[i+1])))
            print('m2',m2)
        return min(m1,m2)
print(Solution().movesToMakeZigzag([1,2,3]))
class Solution:
    def movesToMakeZigzag(self, nums: 'List[int]') -> int:
        m1,m2=0,0
        a=[float('inf')]+nums+[float('inf')]
        n=len(a)
        for i in range(1,n-1,2):
            m1+=max(0,a[i]+1-(min(a[i-1],a[i+1])))
        for i in range(2,n-1,2):
            m2+=max(0,a[i]+1-(min(a[i-1],a[i+1])))
        return min(m1,m2)