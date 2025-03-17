# since we can turn at least k 0's, the minimum number we can return is k
# that means that we can look at a sliding window with width k
# then, we can track a left pointer to track how many 1's are to the left
# need to figure out how to track the 1's to the right
# iterate forward
# if we hit a zero, check if we can still flip any ones
# if yes, subtract one from pool of ones and keep going
# if no, move left pointer forward until hit a zero, which
# will give us a one to flip
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_ones = k
        left = 0
        flipped_ones: list[int] = []
        for i in range(len(nums)):
            curr = nums[i]
            if curr == 1:
                continue
            if len(flipped_ones) < k:
                flipped_ones.append(i)
                continue
            max_ones = max(i - left, max_ones)
            if k < 1:
                left = i + 1
            else:
                left = flipped_ones.pop(0) + 1
                flipped_ones.append(i)
        max_ones = max(len(nums) - left, max_ones)

        return max_ones
