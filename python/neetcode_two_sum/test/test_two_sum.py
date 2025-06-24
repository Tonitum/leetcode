from python.neetcode_two_sum.solution import Solution


class TestTwoSum:
    def test_case_one(self):
        nums = [3,4,5,6]
        target = 7
        assert Solution().twoSum(nums, target) == [0,1]

    def test_case_two(self):
        nums = [4,5,6]
        target = 10
        assert Solution().twoSum(nums, target) == [0,2]
