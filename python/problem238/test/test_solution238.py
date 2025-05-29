from problem238.python.solution import Solution


class TestSolution238:
    def test_case_one(self):
        nums = [1, 2, 3, 4]
        res = Solution().productExceptSelf(nums)
        assert res == [24, 12, 8, 6]
