class Solution:
    def prevPermOpt1(self, A):
        for i in range(len(A)-1,0,-1):#最尾
            if A[i-1]>A[i]:
                print('A[i-1]',A[i-1],'A[i]',A[i])
                m=max(A[i:len(A)])
                print('m',m)
                B=A[i:len(A)]
                print('B',B)
                print('len(B)',len(B))
                for j in range(len(B)):
                    if B[j]==m:
                        tmp=A[i+j]
                        print('A[i+j]',A[i+j])
                        print(A[i-1+j],i-1+j,'tmp')
                        A[i+j]=A[i-1]
                        print('A[i-1+j]項數與值',i-1+j,A[i-1+j])
                        A[i-1]=tmp
                        print('A',A)
                        return A
            else:
                return A
print(Solution().prevPermOpt1([3,2,1]))