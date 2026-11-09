class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        return all(nums[i] == nums[i+1]-1 for i in range(len(nums) - 1))