

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


    def rotate1(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        prefix_slice = nums[len(nums)-k:]
        postfix_slice = nums[:len(nums)-k]
        prefix_slice.extend(postfix_slice)
        nums[:] = prefix_slice



