class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        winner = 0
        current = 1
        for first, second in zip(nums[:-1], nums[1:]):
            if first == second:
                continue
            if second == first + 1:
                current += 1
                # winner = max(winner, current)
            else:
                winner = max(winner, current)
                current = 1
        return max(winner, current)
            