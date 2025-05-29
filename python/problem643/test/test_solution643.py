from problem643.python.solution import Solution


class TestSolution643:
    def test_case_one(self):
        nums = [1,12,-5,-6,50,3]
        k = 4
        assert Solution().findMaxAverage(nums, k) == 12.75

