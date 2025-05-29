class Solution:
    def canJump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return 1

        # iterate through and find all of the indicies that point to target
        earliest_node = len(nums)
        earliest_node = self.get_earliest_jump_point(nums[0:earliest_node])
        jump_count = 1
        while earliest_node > 0:
            earliest_node = self.get_earliest_jump_point(nums[0:earliest_node+1])
            jump_count += 1

        return jump_count

    def get_earliest_jump_point(self, nums: list[int]) -> int:
        nums_length: int = len(nums) - 1
        earliest_node = -1
        for i in range(nums_length - 1, -1, -1):

            difference: int = nums_length - i
            if nums[i] >= difference:
                earliest_node = i
        return earliest_node
