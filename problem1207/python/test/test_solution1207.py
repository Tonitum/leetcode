from problem1207.python.solution import Solution


class TestSolution1207:
    def test_case_one(self):
        arr = [1, 2, 2, 1, 1, 3]
        assert Solution().uniqueOccurrences(arr)

    def test_case_two(self):
        arr = [1, 2]
        assert not Solution().uniqueOccurrences(arr)

    def test_case_three(self):
        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        assert Solution().uniqueOccurrences(arr)
