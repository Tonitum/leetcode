from problem169.python.solution import Solution


class TestSolution169:
    def test_case_one(self):
        solution = Solution()
        nums = [3,2,3]
        res = solution.majorityElement(nums)
        assert res == 3

    def test_case_two(self):
        solution = Solution()
        nums = [2,2,1,1,1,2,2]
        res = solution.majorityElement(nums)
        assert res == 2

