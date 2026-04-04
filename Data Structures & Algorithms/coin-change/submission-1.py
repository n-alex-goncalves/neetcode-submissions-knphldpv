class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float('inf')] * (amount + 1)

        if amount == 0:
            return 0

        for coin in coins:
            if coin <= amount:
                table[coin] = 1

        for i in range(amount):
            if table[i] > 0 and table[i] != float('inf'):
                for coin in coins:
                    if i + coin <= amount:
                        table[i + coin] = min(table[i + coin], table[i] + 1)
        
        return table[amount] if table[amount] != float('inf') else -1