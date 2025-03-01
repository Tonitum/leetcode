from problem45.python.solution import Solution


class TestSolution45:
    def test_case_one(self):
        solution = Solution()
        nums = [2, 3, 1, 1, 4]
        res = solution.canJump(nums)
        assert res == 2

    def test_case_two(self):
        solution = Solution()
        nums = [2, 3, 0, 1, 4]
        res = solution.canJump(nums)
        assert res == 2

    def test_case_three(self):
        solution = Solution()
        nums = [1, 2]
        res = solution.canJump(nums)
        assert res == 1

    def test_case_four(self):
        solution = Solution()
        nums = [1, 2, 3]
        res = solution.canJump(nums)
        assert res == 2

    def test_case_five(self):
        solution = Solution()
        nums = [3, 2, 1]
        res = solution.canJump(nums)
        assert res == 1

    def test_case_six(self):
        solution = Solution()
        nums = [1,1,1,1]
        res = solution.canJump(nums)
        assert res == 3
