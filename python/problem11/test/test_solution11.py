from problem11.python.solution import Solution


class TestSolution11:
    def test_case_one(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        assert Solution().maxArea(height) == 49

    def test_case_two(self):
        height = [10,1,1,10]
        assert Solution().maxArea(height) == 30

    def test_case_three(self):
        height = [10,1,10,1]
        assert Solution().maxArea(height) == 20

    def test_case_four(self):
        height = [10,1,10,10]
        assert Solution().maxArea(height) == 30

    def test_case_five(self):
        height = [0,1,10,10]
        assert Solution().maxArea(height) == 10
