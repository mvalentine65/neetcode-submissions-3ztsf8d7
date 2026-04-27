class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in sorted(Counter(nums).items(), key=lambda tup: tup[1], reverse=True)[0:k]]