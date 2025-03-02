class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output: list[int] = [1] * len(nums)

        prefix_product = 1
        for i in range(1,len(nums)):
            prefix_product = prefix_product * nums[i-1]
            output[i] *= prefix_product

        suffix_product = 1
        for i in range(len(nums)-2,-1,-1):
            suffix_product = suffix_product * nums[i+1]
            output[i] *= suffix_product
        return output


