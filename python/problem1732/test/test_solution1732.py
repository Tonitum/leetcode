from problem1732.python.solution import Solution


class TestSolution1732:
    def test_case_one(self):
        gain = [-5, 1, 5, 0, -7]
        assert Solution().largestAltitude(gain) == 1

    def test_case_two(self):
        gain = [-4,-3,-2,-1,4,3,2]
        assert Solution().largestAltitude(gain) == 0
