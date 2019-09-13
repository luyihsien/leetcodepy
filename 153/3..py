class Solution:
    def maximumSum(self, arr) -> int:
        l=[]
        for i in range(len(arr)):
            s=0
            if arr[:i]==[]:
                l.append(arr[i])
                continue
            for j in range(i):
                s+=arr[j]
                if s<0:
                    s=0
            a1=arr[i]
            a2=arr[:i]
            #print('a2',a2)
            l.append(max(a1,a1+s,a1+(sum(a2)-min(a2))))

            #print(l)


        return max(l)


print(Solution().maximumSum([1,-2,0,3]))
