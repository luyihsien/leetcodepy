class Solution:
    def prevPermOpt1(self, A):
        for i in range(len(A)-1,0,-1):#最尾
            if A[i-1]>A[i]:
                print('A[i-1]',A[i-1],'A[i]',A[i])
                B=A[i:len(A)]
                C=A[i:len(A)]
                #while A[i-1] in C:
                    #C.remove(A[i-1])
                D=[]
                for k in C:
                    if k<A[i-1]:
                        D.append(k)
                m=max(D)
                print('B',B)
                print('len(B)',len(B))
                for j in range(len(B)):
                    if B[j]==m:
                        tmp=A[i+j]
                        #print('A[i+j]',A[i+j])
                        #print(A[i-1+j],i-1+j,'tmp')
                        A[i+j]=A[i-1]
                        #print('A[i-1+j]項數與值',i+j,A[i+j])
                        A[i-1]=tmp
                        print('A',A)
                        return A
            #else:
                #return A
        return A
a=[1,2,3,4]
print(a[:2],a[2:])
#print(Solution().prevPermOpt1([3,2,1]))
print(Solution().prevPermOpt1([1,9,4,6,7]))
print(Solution().prevPermOpt1([3,1,1,3]))
#[1,9,4,6,7]