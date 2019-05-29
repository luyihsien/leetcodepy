class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend([0]*len(nums2))
        j=0
        for i in range(len(nums2)):
            if nums2[i]<nums1[j]:
                nums1.pop()
                print(nums1)
                nums1.insert(j,nums2[i])
            j=j+1

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend([0]*n)
        j=0
        for i in range(len(nums1)):
            if nums2[j]<nums1[i]:
                nums1.remove(0)
                nums1.insert(i,nums2[j])
                j=j+1

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n0=len(nums1)-n
        j=0
        for i in range(n0):
            if nums2[j]<nums1[i]:
                nums1.remove(0)
                nums1.insert(i,nums2[j])
                j=j+1
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n0=len(nums1)-n
        j=0
        for i in range(n0):
            while nums2[j]<nums1[i]:
                nums1.remove(0)
                nums1.insert(i,nums2[j])
                j=j+1
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n=len(nums1)
        j=0
        for i in range(n):
            if nums2[j]<nums1[i] and nums2[j]<len(nums2):
                nums1.remove(0)
                nums1.insert(i,nums2[j])
                j=j+1
            if nums1[i]==0 and nums2[j]<len(nums2):
                nums1[i]=nums2[j]