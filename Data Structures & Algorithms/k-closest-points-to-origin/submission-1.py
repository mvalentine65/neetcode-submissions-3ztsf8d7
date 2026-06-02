class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        calc_squared_distance = lambda pair: pair[0]*pair[0] + pair[1]*pair[1]
        for point in points:
            heapq.heappush_max(heap, (calc_squared_distance(point), point))
            if len(heap) > k:
                heapq.heappop_max(heap)
        return [pair[1] for pair in heap]
