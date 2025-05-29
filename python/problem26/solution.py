class Solution:
    def removeDuplicates1(self, nums: list[int]) -> int:
        target_range = len(nums)
        i = 1
        while i < target_range:
            if nums[i] == nums[i - 1]:
                _ = nums.pop(i)
                target_range -= 1
            else:
                i += 1
        return i

    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)
