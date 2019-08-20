import collections
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        d=collections.Counter()
        def dfs(root,l):
            if root != None:
                l+=1
                if d[l]==0:
                    d[l]=[root.val]
                else:
                    d[l].append(root.val)
                dfs(root.left,l)
                dfs(root.right,l)
        dfs(root,0)
        for i in d:
            d[i]=sum(d[i])


        return d.most_common()[0][0]
a=TreeNode(1)
a.left=TreeNode(7)
a.right=TreeNode(0)
a.left.left=TreeNode(7)
a.left.right=TreeNode(-8)
print(Solution().maxLevelSum(a))