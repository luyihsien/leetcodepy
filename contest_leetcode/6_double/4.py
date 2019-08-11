class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        convert={}
        usage=set()
        for i in range(len(str1)):
            if str1[i] not in convert:
                convert[str1[i]]=str2[i]
            else:
                if str2[i]!=convert[str1[i]]:
                    return False
            usage.add(str2[i])
        if len(usage)==26 and str1!=str2:
            return False
        return True
a='abcdefghijklmnopqrstuvwxyz'
b=a[::-1]

Solution().canConvert(a,)