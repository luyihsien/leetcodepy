class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root) -> int:
        l=[]
        def traversal(root):
            if root==None:
                return
            if root!=None:
                l.append(root.val)
                print(l)
                traversal(root.left)
                traversal(root.right)
        traversal(root)
        print('last',l)
        return max(l)-min(l)
a=TreeNode(8)
a.left=TreeNode(3)
a.left.left=TreeNode(1)
a.left.right=TreeNode(6)
a.left.right.left=TreeNode(4)
a.left.right.right=TreeNode(7)
a.right=TreeNode(10)
a.right.right=TreeNode(14)
a.right.right.left=TreeNode(13)
print(Solution().maxAncestorDiff(a))