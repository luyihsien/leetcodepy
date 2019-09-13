class Solution:
    """
    @param str: The identifier need to be judged.
    @return: Return if str is a legal identifier.
    """
    def isLegalIdentifier(self, str):
        # Write your code here.
        a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
        n0='0123456789'
        n=len(str)
        if n==0:
            return False
        if str[0] in n0:
            return False
        for i in range(1,n):
            if not (str[i] in a or str[i] in n0):
                return False
        return True