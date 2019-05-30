#88
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        print(m,n)
        while m>0 and n>0:
            if nums2[n-1]>nums1[m-1]:
                nums1[m+n-1]=nums2[n-1]
                n=n-1
                return nums1
            else:#這裡就跑出去了#對，但原因不在此，因為連while都沒進去，何來判斷其m==0
                print(nums1)
                nums1[m+n-1],nums1[m-1]=nums1[m-1],nums1[m+n-1]
                m=m-1
        if m==0 and n>0:
            print('nums1都比nums2剩得多未換前',nums1)
            nums1[:n]=nums2[:n]
            print('nums1都比nums2剩得多未換後', nums1)
            return nums1
print(Solution().merge([0],0,[1],1))#此case
'''
解答错误显示详情 输入[0] 0 [1] 1
输出 [0]
预期结果 [1]
縮排小心
'''

#100
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSametree(p.right, q.right)

class Solution:
    def isSameTree(self, p,q) :
        def check(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            if p.val!=q.val:
                return False
        return check(p.left,q.left) and check(p.right,q.right)
'''
AttributeError: 'Solution' object has no attribute 'isSametree'
'''
'''
输入 [1,2,3] [1,2,3]
输出 null
预期结果 true
'''
#101
'''
class Solution:
    def isSymmetric(self, root):
        def check(node1,node2):
'''