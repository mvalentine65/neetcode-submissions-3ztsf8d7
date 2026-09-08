class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        BUYING = 0
        SELLING = 1
        dp = [[None] * n for _ in range(2)]
        def dfs(i: int, trade_state: int) -> int:
            if i >= n:
                return 0
            if dp[trade_state][i] is not None:
                return dp[trade_state][i]

            cooldown = dfs(i + 1, trade_state)
            if trade_state == BUYING:
                buy = dfs(i + 1, SELLING) - prices[i]
                dp[BUYING][i] = max(buy, cooldown)
            else:
                sell = dfs(i+2, BUYING) + prices[i]
                dp[SELLING][i] = max(sell, cooldown)
            return dp[trade_state][i]
        return dfs(0, BUYING)
