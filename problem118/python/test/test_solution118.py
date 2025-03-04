from problem118.python.solution import Solution


class TestSolution118:
    def test_case_one(self):
        res = Solution().generate(5)
        assert res == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    def test_case_two(self):
        res = Solution().generate(1)
        assert res == [[1]]
