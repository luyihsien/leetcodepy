import heapq
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        heapq.heapify(A)#創一個時複O(n)button up建構的min heap#要讓它變大就是一直讓最小的出去故適用min heap結合pop而不是max heap
        for i in range(K):
            p = heapq.heappop(A)
            print(p)
            if p == 0:#一直換它就好故break
                break
            heapq.heappush(A, -p)
        return sum(A)
Solution().largestSumAfterKNegations([-2,5,0,2,-2],3)