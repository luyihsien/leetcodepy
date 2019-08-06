class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        b=A.copy()
        b.sort()
        d={}
        for i in range(len(A)):
            d[i]=A[i]
        while K:
            if b[0]>=0:
                if K == 0:
                    break
                for i in d:
                    if K==0:
                        break
                    if d[i]==b[0]:
                        A[i]=-A[i]
                        d[i]=-b[0]
                        K = K - 1
                        print('K',K)
                        if K == 0:
                            break

                        b=A.copy()
                        b.sort()



            for i in b:
                if K==0:
                    break

                if i<0:
                    for j in d:#為何j一動也不動??#後面被break掉故一直重來#將第30列break改成continue
                        if d[j]==i:
                            A[j]=-A[j]
                            d[j]=-i
                            K = K - 1
                            print('K', K, 'A', A)
                            if K == 0:
                                break

                        b=A.copy()
                        b.sort()

                    print('b', b, 'A', A,'d',d)
                    print('K', K)

        return sum(A)
'''
print(Solution().largestSumAfterKNegations([4,2,3],1))
print(Solution().largestSumAfterKNegations(A = [3,-1,0,2], K = 3))
print(Solution().largestSumAfterKNegations(A = [2,-3,-1,5,-4], K = 2))
'''
print(Solution().largestSumAfterKNegations([2,-3,-1,5,-4]
,2))
"""
A [-2, 5, 0, 2, 2]
A [-2, 5, 0, 2, -2]
A [-2, 5, 0, 2, 2]
7 因為字典value被複寫而同key值只能放一個座標...
<想法:更新字典>
預期11
"""