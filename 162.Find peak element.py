#https://blog.csdn.net/fuxuemingzhu/article/details/79633332
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid=(right+left)//2
            print('mid',mid)
            if nums[mid]<nums[mid+1]:
                print('nums[mid]',nums[mid])
                left=mid+1
                print('left',left)
            else:
                right=mid
                print('right',right)
        return left
print(Solution().findPeakElement([1,2,1,3,5,6,4]))
class Solution(object):
    def findPeakElement(self, nums):
        nums.insert(0,float('-inf'))
        nums.insert(len(nums),float('-inf'))
        print(nums)
        n=[]
        for i in range(1,len(nums)):
            n.append(nums[i]-nums[i-1])
            print('n',n)
            for i in range(1,len(n)):
                print('n[i-1]',n[i-1],'n[i]',n[i])

#print(Solution().findPeakElement([1,2,1,3,5,6,4]))
print(Solution().findPeakElement([1]))
