class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit: int = 0
        buy_price = prices[0]
        sell_price = 0
        possible_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < sell_price or prices[i] < buy_price:
                profit += possible_profit
                possible_profit = 0
                sell_price = 0
                buy_price = prices[i]
                continue

            if prices[i] - buy_price > possible_profit:
                sell_price = prices[i]
                possible_profit = prices[i] - buy_price

        profit += possible_profit

        return profit
