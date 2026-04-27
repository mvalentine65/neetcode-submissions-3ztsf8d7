class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = list(Counter(nums).items())
        counts.sort(key=lambda tup: tup[1])
        return [x for x, _ in counts[-k:]]
        # return [num for num, _ in sorted(Counter(nums).items(), key=lambda tup: tup[1], reverse=True)[0:k]]