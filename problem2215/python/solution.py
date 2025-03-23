class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        all_nums: dict[int, int] = {}
        unique_left: list[int] = []
        unique_right: list[int] = []

        for num in nums1:
            if num in all_nums:
                continue
            all_nums[num] = 1

        for num in nums2:
            if num in all_nums.keys():
                all_nums[num] = all_nums[num] + 1
                continue
            all_nums[num] = 0
            unique_right.append(num)

        for num in nums1:
            if all_nums[num] == 1:
                unique_left.append(num)
                all_nums[num] = 0

        return [unique_left, unique_right]
