class Solution {
    public int maxProfit(int[] prices) {
        int valley = prices[0];
        int profit = 0;

        for (int i = 1; i < prices.length; i++) {
            int curr = prices[i];
            if (curr < valley) {
                valley = curr;
                continue;
            }
            int diff = curr - valley;
            if (diff > profit) {
                profit = diff;
            }
        }
        return profit;
    }
}
