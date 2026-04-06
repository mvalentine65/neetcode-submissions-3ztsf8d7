class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current, most = 0, 0
        for num in nums:
            if num == 1:
                current += 1
                most = max(most, current)
            else:
                current = 0
        return most