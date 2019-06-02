class Solution(object):
    def gcdOfStrings(self, str1, str2):
        a=0
        if len(str1)>len(str2):
            for i in range(len(str2)-1):
                for j in range(i+1,len(str2)):
                    if str2.replace(str2[i:j+1],'')=='' and str1.replace(str2[i:j+1],'')=='':
                        a=str2[i:j+1]
        else:
            for i in range(len(str2)-1):
                for j in range(i+1,len(str2)):
                    if str2.replace(str2[i:j+1],'')=='' and str1.replace(str2[i:j+1],'')=='':
                        a=str1[i:j+1]
            if a==0:
                return ""
            else:
                return a
print(Solution().gcdOfStrings("ABD",'ABC'))
