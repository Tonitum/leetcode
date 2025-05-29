class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        target_range = len(nums)
        i = 2
        while i < target_range:
            if nums[i] == nums[i - 1]:
                if nums[i-1] == nums[i-2]:
                    _ = nums.pop(i)
                    target_range -= 1
                else:
                    i += 1
            else:
                i += 1
        return i

