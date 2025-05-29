from problem283.python.solution import Solution


class TestSolution283:
    def test_case_one(self):
        nums = [0, 1, 0, 3, 12]
        Solution().moveZeroes(nums)
        assert nums == [1, 3, 12, 0, 0]

    def test_case_two(self):
        nums = [0]
        Solution().moveZeroes(nums)
        assert nums == [0]

    def test_case_three(self):
        nums = [0,0,1]
        Solution().moveZeroes(nums)
        assert nums == [1,0,0]
