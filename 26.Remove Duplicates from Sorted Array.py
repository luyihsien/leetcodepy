'''
Question
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
'''
'''
class Solution:
    def removeDuplicates(self, nums):
        a=set()
        for i in nums:
            b=str(i)
            if b not in a:
                a.add(b)
            else:
                nums=nums.remove(b)
        return len(i)
'''

'''
class Solution:
    def removeDuplicates(self, nums):
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0
            elif d[nums[i]] != 0:

                print(nums)
        return len(i)


class Solution:
    def removeDuplicates(self, nums):
        a = set()
        b = []
        for i in range(len(nums)):
            c = str(i)
            if c not in a:
                a.add(c)
            else:
                b.appand(i)
        for i in range(len(b)):
            del nums[int(b[i])]

        return len(nums)
'''
a=[1,2,4]
for i in a:#IndexError: list index out of range
    print(i)#[1,2,4]
    a.remove(a[i])
    print(a)
b=1
if not [] :
    print(b)