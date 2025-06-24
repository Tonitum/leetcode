class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Questions I would ask here:
        #   is there guaranteed to be a solution?
        #   what should the sentinel value be, if there is not?
        seen: dict[int, int] = {}

        # time complexity O(n)
        # space complexity O(n)
        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff in seen:
                return [seen[diff], i]
            seen[curr] = i

        return [-1,-1]
