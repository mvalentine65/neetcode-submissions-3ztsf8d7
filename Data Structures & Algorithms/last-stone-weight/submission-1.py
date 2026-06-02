class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            y, x = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if y == x:
                continue
            heapq.heappush_max(stones,y-x)
        if stones:
            return stones[0]
        else:
            return 0
