# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
'''
if not 0 and not 0:
    print(1)
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:#不可以if ??因為若是p and q皆None的前面已經return了，所以應該可以#因為p q 是node不是純value故址只要不是None就算value是0 其boolean也是ture
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
a=TreeNode(0)
a.left=None
a.right=None
if TreeNode:
    print('4')#4，會執行