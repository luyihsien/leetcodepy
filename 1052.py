class Solution:
    def prevPermOpt1(self, A):
        for i in range(len(A)-1,0,-1):#最尾
            if A[i-1]>A[i]:
                print('A[i-1]',A[i-1],'A[i]',A[i])
                B=A[i:len(A)]
                C=A[i:len(A)]
                for j in C:
                    if A[i-1]==C[j]:
                        C.remove(A[i-1])
                m=max(C)
                print('B',B)
                print('len(B)',len(B))
                for j in range(len(B)):
                    if B[j]==m:
                        tmp=A[i+j]
                        print('A[i+j]',A[i+j])
                        print(A[i-1+j],i-1+j,'tmp')
                        A[i+j]=A[i-1]
                        print('A[i-1+j]項數與值',i+j,A[i+j])
                        A[i-1]=tmp
                        print('A',A)
                        return A
            #else:
                #return A
        return A
#print(Solution().prevPermOpt1([3,2,1]))
print(Solution().prevPermOpt1([1,9,4,6,7]))
print(Solution().prevPermOpt1([3,1,1,3]))
#[1,9,4,6,7]