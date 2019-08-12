class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        convert={}
        usage=set()
        for i in range(len(str1)):
            if str1[i] not in convert:
                print('convert',convert)
                convert[str1[i]]=str2[i]
            else:
                if str2[i]!=convert[str1[i]]:
                    print('convert',convert)
                    return False
            usage.add(str2[i])
            print('usage',usage,len(usage))
            print('convert',convert)
        if len(usage)==26 and str1!=str2:
            return False
        return True
a='abcdefghijklmnopqrstuvwxyz'
b=a[::-1]
print(b)
c='abcd'
d='bcda'
print(Solution().canConvert(a,b))
print(Solution().canConvert(c,d))
'''
"abcdefghijklmnopqrstuvwxyz"
"bcdefghijklmnopqrstuvwxyza"
'''
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        s1 = dict()
        for i, ch in enumerate(str1):
            if ch not in s1:
                s1[ch] = list()
            s1[ch].append(i)
        s2 = dict()
        for i, ch in enumerate(str2):
            if ch not in s2:
                s2[ch] = list()
            s2[ch].append(i)
        if len(s1) == len(s2) == 26 and str1 != str2:
            return False

        for k, v in s1.items():
            pivot = str2[v[0]]
            for pos in v:
                if str2[pos] != pivot:
                    return False

        return True
print(Solution().canConvert('abcd','bcda'))