class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root) -> int:
        def traversal(root):
            res =0#在def外沒用
            if root==None:
                return
            if root!=None:
                if root.left!=None:
                    res=max(res,abs(root.val-root.left.val))
                if root.right!=None:
                    res=max(res,abs(root.val-root.right.val))
        traversal(root)