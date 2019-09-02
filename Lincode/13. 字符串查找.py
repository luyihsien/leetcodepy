class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        n = len(source)
        k = len(target)
        for i in range(n - k + 1):
            if source[i:i + k] == target:
                return i
        return -1
