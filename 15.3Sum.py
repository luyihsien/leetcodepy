'''
a=[1,2]
print(a)
nums=[1]
d=[]
for i in nums:
    print(i)
    d.append(-nums[i])

print(d)

class Solution:
    def threeSum(self, nums):
        c=[]
        d=[]
        for i in range(len(nums)):
            d.append(-nums[i])
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                a=nums[i]+nums[j]
                if a in d:
                    c.extend([[nums[i],nums[j],-(nums[i]+nums[j])].sort()])
        return c

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        class Solution:
            def threeSum(self, nums):
                a = [0] * len(nums)
                b = a - nums
                c = []
                for i in range(len(nums)):
                    for j in range(i + 1, len(nums)):
                        if (nums[i] + nums[j]) in b:
                            c.extend([[nums[i], nums[j], -(nums[i] + nums[j])].sort()])
                return c
class Solution:
    def threeSum(self, nums):
        a=[0]*len(nums)
        d=[]
        for i in nums:
            b=a[i]-nums[i]
            d.append(b)
        c=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]) in d:
                    c.extend([[nums[i],nums[j],-(nums[i]+nums[j])].sort()])
        return c

IndexError: list index out of range
Line 6 in threeSum (Solution.py)
Line 26 in __helper__ (Solution.py)
Line 40 in _driver (Solution.py)
Line 51 in <module> (Solution.py)

class Solution:
    def threeSum(self, nums):
        c=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]) in -nums:
                    c.extend([[nums[i],nums[j],-(nums[i]+nums[j])].sort()])
        return c
'''

'''
输入
[-1,0,1,2,-1,-4]
输出
[null,null,null,null,null,null,null,null,null]
预期结果
[[-1,-1,2],[-1,0,1]]
'''


class Solution:
    def threeSum(self, nums):
        c = []
        d = []
        for i in range(len(nums)):
            d.append(-nums[i])
        print('d',d)
        for i in range(len(nums)):
            print('i',i)
            for j in range(i + 1, len(nums)):
                print('j',j)
                a = nums[i] + nums[j]
                print('nums[i]+nums[j]',nums[i]+nums[j])

                if a in d:
                    print('H')
                    print([nums[i], nums[j], -(nums[i] + nums[j])])
                    c.extend([[nums[i], nums[j], -(nums[i] + nums[j])].sort()])
                    print('c過程',c)
        print('c最終',c)
        return c
Solution().threeSum([-1,0,1,2,-1,-4])
print(set([1,0,1],[1,1,0],[1,0,1]))