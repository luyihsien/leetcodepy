class Solution:
    def nextPermutation(self, nums):
        n=-1
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                n=i-1
                break
        if n==-1:
            nums.reverse()
        else:
            for i in range(len(nums)-1,n,-1):
                if nums[n]<nums[i]:
                    nums[n],nums[i]=nums[i],nums[n]
a=[1,2,3,4,5]
a[3:].reverse()#TypeError: can only assign an iterable
print(a)#[1, 2, 3, 4, 5]
a[3:][::-1]
print(a)#[1, 2, 3, 4, 5]
class Solution:#自己的正確答案
    def nextPermutation(self, nums):
        n=-1
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                n=i-1
                break
        if n==-1:
            nums.reverse()
        else:
            for i in range(len(nums)-1,n,-1):
                if nums[n]<nums[i]:
                    nums[n],nums[i]=nums[i],nums[n]
                    nums[n+1:]=nums[n+1:][::-1]
                    break
reversed(a[3:])#None
a = [1, 2, 3]
b = a
del a[:]
print(b)#[]

a = [1, 2, 3]
b = a
a = []
print(b)#[1, 2, 3]
a=[1,2,3]
b=a
b=[]
del b[:]
print(a)#皆[1,2,3] 因是b指針指向a不是a指針指向b