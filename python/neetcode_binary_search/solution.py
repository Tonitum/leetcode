class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high= len(nums) - 1
        while low < high:
            mid = int(low + ((high - low) / 2))
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid
                continue
            high = mid - 1
            continue
        return -1
