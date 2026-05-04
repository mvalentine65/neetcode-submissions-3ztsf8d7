class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        working = []
        n = len(nums)
        def backtrack(i: int) -> None:
            if i == n:
                subsets.add(tuple(working))
                return
            working.append(nums[i])
            backtrack(i+1)
            working.pop()
            backtrack(i+1)
        backtrack(0)
        return [list(tup) for tup in subsets]