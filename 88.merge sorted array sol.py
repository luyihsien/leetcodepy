import copy
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result = copy.deepcopy(nums1)[:m]
        i,j,idx=0,0,0
        while j<n and i<m:
            if result[i] < nums2[j]:
                nums1[idx] =  result[i]
                i+=1
                idx+=1
            else:
                nums1[idx] =  nums2[j]
                j+=1
                idx+=1
        while i < m:
                nums1[idx] =  result[i]
                i+=1
                idx+=1
        while j < n:
                nums1[idx] = nums2[j]
                j+=1
                idx+=1
        print(nums1)
print(Solution().merge([2,3,4,0,0,0,0,0,0,0],3,[1,1,1,1,2,5,6],7))