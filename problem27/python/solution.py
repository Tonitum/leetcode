class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        non_val_count = 0
        i = 0
        target_range = len(nums)
        while i < target_range:
            if nums[i] == val:
                _ = nums.pop(i)
                nums.append(0)
                target_range = target_range - 1
            else:
                i = i + 1
                non_val_count += 1
        return non_val_count
