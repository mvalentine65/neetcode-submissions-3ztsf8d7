class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        working = []
        result = []
        def backtrack(i: int, total: int) -> None:
            if i == len(nums):
                if total == target:
                    result.append(working[:])
                return
            backtrack(i+1, total)
            added = 0
            while total < target:
                added += 1
                total += nums[i]
                working.append(nums[i])
                backtrack(i+1, total)
            for _ in range(added):
                working.pop()
        backtrack(0, 0)
        return result