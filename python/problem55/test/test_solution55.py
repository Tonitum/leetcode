from problem55.python.solution import Solution


class TestSolution55:
    def test_case_one(self):
        solution = Solution()
        nums = [2, 3, 1, 1, 4]
        assert solution.canJump(nums)

    def test_case_two(self):
        solution = Solution()
        nums = [3, 2, 1, 0, 4]
        assert not solution.canJump(nums)
