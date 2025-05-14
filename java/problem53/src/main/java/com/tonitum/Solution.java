package com.tonitum;

class Solution {
    public int maxSubArray(int[] nums) {
        int runningSum = 0;
        int maxSum = 0;
        int largestNegative = 1;
        for (int i = 0; i < nums.length; i++) {
            if (runningSum + nums[i] <= 0) {
                runningSum = 0;
                if (nums[i] > largestNegative || largestNegative == 1) {
                    largestNegative = nums[i];
                }
                continue;
            }
            runningSum += nums[i];
            if (runningSum > maxSum) {
                maxSum = runningSum;
            }
        }
        if (maxSum == 0) {
            return largestNegative;
        }
        return maxSum;
    }
}

