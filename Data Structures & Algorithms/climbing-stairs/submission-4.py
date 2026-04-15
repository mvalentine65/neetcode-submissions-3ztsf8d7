from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def recurse(num: int) -> int:
            if num <= 2:
                return num
            else:
                return recurse(num - 1) + recurse(num - 2)
        return recurse(n)