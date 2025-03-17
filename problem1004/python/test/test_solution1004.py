from problem1004.python.solution import Solution


class TestSolution1004:
    def test_case_one(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        assert Solution().longestOnes(nums, k) == 6

    def test_case_two(self):
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3
        assert Solution().longestOnes(nums, k) == 10

    def test_case_three(self):
        nums = [0, 0, 1, 1, 1, 0, 0]
        k = 0
        assert Solution().longestOnes(nums, k) == 3

    def test_case_four(self):
        nums = [0, 0, 1, 1]
        k = 1
        assert Solution().longestOnes(nums, k) == 3
