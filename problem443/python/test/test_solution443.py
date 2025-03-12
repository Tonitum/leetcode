from problem443.python.solution import Solution


class TestSolution443:
    def test_case_one(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        res = Solution().compress(chars)
        assert res == 6

    def test_case_two(self):
        chars = ["a"]
        res = Solution().compress(chars)
        assert res == 1

    def test_case_three(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        res = Solution().compress(chars)
        assert res == 4
        assert chars == ["a", "b", "1", "2"]
