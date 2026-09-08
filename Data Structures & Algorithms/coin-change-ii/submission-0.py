class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def recurse(total: int, coin_index: int) -> int:
            if total == 0:
                return 1
            if coin_index >= len(coins):
                return 0
            if memo[coin_index][total] != -1:
                return memo[coin_index][total]
            
            result = 0
            if total >= coins[coin_index]:
                result = recurse(total, coin_index + 1)
                result += recurse(total - coins[coin_index], coin_index)
            
            memo[coin_index][total] = result
            return result

        return recurse(amount, 0)