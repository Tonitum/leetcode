from problem724.python.solution import Solution


class TestSolution724:
    def test_case_one(self):
        nums = [1, 7, 3, 6, 5, 6]
        assert Solution().pivotIndex(nums) == 3

    def test_case_two(self):
        nums = [1, 2, 3]
        assert Solution().pivotIndex(nums) == -1

    def test_case_three(self):
        nums = [2,1,-1]
        assert Solution().pivotIndex(nums) == 0
