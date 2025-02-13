class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            current_price = prices[i]
            if current_price < lowest_price:
                lowest_price = current_price
                continue
            possible_profit = current_price - lowest_price
            if possible_profit > profit:
                profit = possible_profit
            

        return profit
