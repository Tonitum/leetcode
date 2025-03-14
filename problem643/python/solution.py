class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[:k]) 
        max_avg = sum(nums[:k])  / k
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i-k] + nums[i]
            curr_avg = current_sum / k
            if curr_avg > max_avg:
                max_avg = curr_avg
        return max_avg
        
