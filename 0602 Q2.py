lass Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        s = dict()
        for row in matrix:
            first = ''.join(map(str, row))
            second = ''.join(map(lambda x: str(1 - x), row))
            if first not in s: s[first] = 1
            else: s[first] += 1
            if second not in s: s[second] = 1
            else: s[second] += 1
        rtn = 0
        for key in s:
            rtn = max(rtn, s[key])
        return rtn