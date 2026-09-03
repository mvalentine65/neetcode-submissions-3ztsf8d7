class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l1+1) for _ in range(l2+1)]

        for y in range(1,l2+1):
            for x in range(1,l1+1):
                if text2[y-1] == text1[x-1]:
                    dp[y][x] = 1 + dp[y-1][x-1]
                else:
                    dp[y][x] = max(dp[y-1][x], dp[y][x-1])
        
        return dp[-1][-1]
                