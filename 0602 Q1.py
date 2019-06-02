class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        rtn = 0
        n1 = len(str1)
        n2 = len(str2)
        for i in range(1, min(n1, n2) + 1):
            if n1 % i == 0 and n2 % i == 0 and str1 == str1[:i] * (n1 // i) and str2 == str1[:i] * (n2 // i):
                rtn = i
        return str1[:rtn]