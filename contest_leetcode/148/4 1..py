num=[9,6,1,6,2]
for i in range(0,len(num)-2,2):
    print(i)
print(num)

class Solution:
    def movesToMakeZigzag(self, nums: 'List[int]') -> int:
        n1=0
        n2=0
        b=nums.copy()
        for i in range(0,len(nums)-2,2):
            print('nums[i],nums[i+1],nums[i+2]',nums[i],nums[i+1],nums[i+2])
            if not (nums[i+1]>nums[i] and nums[i+1]>nums[i+2]):
                while nums[i+1]<=nums[i]:
                    nums[i]=nums[i]-1
                    print('nums[i]', nums[i])
                    n1=n1+1
                while nums[i+1]<=nums[i+2]:
                    nums[i+2]=nums[i+2]-1
                    print('nums[i+2]',nums[i+2])
                    n1=n1+1
            n = i + 2
        if n<len(nums)-1:
            if nums[n+1]<nums[n]:
                nums[n]=nums[n]-1
                n1=n1+1



        for i in range(0,len(nums)-2,2):
            if not (b[i+1]<b[i] and b[i+1]<b[i+2]):
                while b[i+1]>=b[i]:
                    b[i+1]=b[i+1]-1
                    n2=n2+1
                while b[i+1]>=b[i+2]:
                    b[i+1]=b[i+1]-1
                    n2=n2+1
        n=i+2
        if n < len(nums) - 1:
            if nums[n + 1] > nums[n]:
                nums[n+1]=nums[n+1] - 1
                n2 = n2 + 1
        print('b',b)
        return min(n1,n2)


print(Solution().movesToMakeZigzag([7,4,8,9,7,7,5]))
print(Solution().movesToMakeZigzag([1,2,3]))
print(Solution().movesToMakeZigzag([10,1,1,6,6,6,1,8,8,5,1,2,6,6,6,4,4,8,7,1]))


