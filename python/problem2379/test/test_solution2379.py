from problem2379.python.solution import Solution


class TestSolution2379:
    def test_case_one(self):
        blocks = "WBBWWBBWBW"
        k = 7
        res = Solution().minimumRecolors(blocks, k)
        assert res == 3

    def test_case_two(self):
        blocks = "BBBWWBBWBW"
        k = 3
        res = Solution().minimumRecolors(blocks, k)
        assert res == 0

    def test_case_three(self):
        blocks = "BWWWBB"
        k = 6
        res = Solution().minimumRecolors(blocks, k)
        assert res == 3

    def test_case_four(self):
        blocks = "WWBBBWBBBBBWWBWWWB"
        k = 16
        res = Solution().minimumRecolors(blocks, k)
        assert res == 6
