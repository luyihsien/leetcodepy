# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root) -> int:
        d = 0
        if root.left != None:
            d = max(d, abs(root.val - root.left.value))
        if root.right != None:
            d = max(d, abs(root.val - root.right.value))
class Solution:
    def maxAncestorDiff(self, root) -> int:
        l=[]
        def traversal(root):
            if root!=None:
                l.append(root.val)
            if root.left!=None:
                l.append(root.left.val)
            if root.right!=None:
                l.append(root.right.val)