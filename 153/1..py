#參考世3排名
class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        if start>destination:
            start,destination=destination,start
        if start==destination:
            return 0
        return min(sum(distance[start:destination]),sum(distance[destination:]+distance[:start]))
print(Solution().distanceBetweenBusStops([7,10,1,12,11,14,5,0],7,2))
