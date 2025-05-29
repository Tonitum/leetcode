from problem122.python.solution import Solution


class TestSolution122:
    def test_case_one(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected_res = 7
        solution = Solution()
        res = solution.maxProfit(prices)
        assert res == expected_res

    def test_case_two(self):
        prices = [1, 2, 3, 4, 5]
        expected_res = 4
        solution = Solution()
        res = solution.maxProfit(prices)
        assert res == expected_res

    def test_case_three(self):
        prices = [7, 6, 4, 3, 1]
        expected_res = 0
        solution = Solution()
        res = solution.maxProfit(prices)
        assert res == expected_res

    def test_case_four(self):
        prices = [6, 1, 3, 2, 4, 7]
        expected_res = 7
        solution = Solution()
        res = solution.maxProfit(prices)
        assert res == expected_res

    def test_case_five(self):
        prices = [1, 2, 0, 1]
        expected_res = 2
        solution = Solution()
        res = solution.maxProfit(prices)
        assert res == expected_res
