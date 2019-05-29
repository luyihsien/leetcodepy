class Solution:
    def merge(self,nums1,m,nums2,n):
        while m>0 and n>0 :
            if nums1[m-1]<nums2[n-1]:
                nums1[m-1+n]=nums2[n-1]
                print('nums1[m-1+n]',nums1[m-1+n])
                print(nums1)
                n=n-1
            else:
                nums1[m-1+n],nums1[m-1]=nums1[m-1],nums1[m-1+n]
                print('nums1',nums1)
                m=m-1
        if m==0 and n>0:
            nums1[:n]=nums2[:n]
        print(nums1)
print(Solution().merge([2,3,4,0,0,0,0,0,0,0],3,[1,1,1,1,2,5,6],7))