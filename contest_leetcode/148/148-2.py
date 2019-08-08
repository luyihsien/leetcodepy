# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root, n: int, x: int) -> bool:
        def size(root):
            if not root:
                return 0
            return size(root.left)+size(root.right)+1
        def find(root,x):#利用None或root為基底，結合加減乘除與邏輯運算，配合return
            if not root:
                return None
            if root.val==x:
                return root
            l,r=find(root.left,x),find(root.right,x)#x勿漏
            return l if l else r
        x=find(root,x)
        A,B=size(x.left),size(x.right)
        return max(A,B,n-1-A-B)*2>n