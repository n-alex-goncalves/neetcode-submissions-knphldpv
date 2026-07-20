class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # tabulation
        if amount == 0:
            return 0

        table = [-1] * (amount + 1)
        
        for coin in coins:
            if coin > amount:
                continue
            table[coin] = 1
        
        for i in range(amount + 1):
            if table[i] != -1:
                for coin in coins:
                    if i + coin > amount:
                        continue
                    if table[i + coin] == -1:
                        table[i + coin] = table[i] + 1
                    else:
                        table[i + coin] = min(table[i] + 1, table[i + coin])
        
        return table[amount]

        