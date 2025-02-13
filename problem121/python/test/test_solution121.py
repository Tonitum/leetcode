from problem121.python.solution import Solution


class TestSolution121:
    def test_case_one(self):
        prices = [7,1,5,3,6,4]
        expected_res = 5
        solution = Solution()
        res = solution.maxProfit(prices)
        assert res == expected_res

    def test_case_two(self):
        prices = [7,6,4,3,1]
        expected_res = 0
        solution = Solution()
        res = solution.maxProfit(prices)
        assert res == expected_res

    def test_case_three(self):
        prices = [1,2]
        expected_res = 1
        solution = Solution()
        res = solution.maxProfit(prices)
        assert res == expected_res

    def test_case_four(self):
        prices = [1,2,4]
        expected_res = 3
        solution = Solution()
        res = solution.maxProfit(prices)
        assert res == expected_res

    def test_case_five(self):
        prices = [2,2,5]
        expected_res = 3
        solution = Solution()
        res = solution.maxProfit(prices)
        assert res == expected_res
