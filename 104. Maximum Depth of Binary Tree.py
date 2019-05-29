h=0#UnboundLocalError: local variable 'h' referenced before assignment
class Solution:# 不會有複算h的問題嗎?
    # h=0#UnboundLocalError: local variable 'h' referenced before assignment
    def maxDepth(self, root):

        if root:
            h += 1
        if not root.left and not root.right:
            return h
        if not root.left:
            self.maxDepth(root.right)
        if not root.right:
            self.maxDepth(root.left)
            return h
#print(Solution().maxDepth(1))
