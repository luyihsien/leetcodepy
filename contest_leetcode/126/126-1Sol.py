#hanshaohey 世界排名第2
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        lts='abcdefghijklmnopqrstuvwxyz'
        ans=[]
        for lt in lts:
            num=min(s.count(lt) for s in A)
            print('num',num)
            ans.extend([lt]*num)
            print('ans',ans)
        return ans
Solution().commonChars(["bella","label","roller"])