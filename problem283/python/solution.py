class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        touched_count = len(nums)
        while i < touched_count:
            curr = nums[i]
            if curr != 0:
                i = i + 1
                continue
            nums[:] = nums[0:i] + nums[i+1:] if i < len(nums) else nums[0:i]
            nums.append(0)
            touched_count -= 1
