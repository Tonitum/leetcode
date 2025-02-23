class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        target = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            curr = nums[i]
            distance = target - i
            if curr >= distance:
                target = i
                if i == 0:
                    return True

        return False
