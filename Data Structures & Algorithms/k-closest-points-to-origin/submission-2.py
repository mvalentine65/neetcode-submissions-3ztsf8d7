class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        calc_squared_distance = lambda x,y: x*x + y*y
        distances = [(calc_squared_distance(point[0], point[1]), point) for point in points]
        heapq.heapify(distances)
        return [pair[1] for pair in heapq.nsmallest(k, distances)]
