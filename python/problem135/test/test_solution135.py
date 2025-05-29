from problem135.python.solution import Solution


class TestSolution135:
    def test_case_one(self):
        ratings = [1, 0, 2]
        expected_count = 5
        solution = Solution()
        res1 = solution.candy(ratings)
        assert expected_count == res1

    def test_case_two(self):
        ratings = [1, 2, 2]
        expected_count = 4
        solution = Solution()
        res1 = solution.candy(ratings)
        assert expected_count == res1

    def test_case_three(self):
        ratings = [1, 3, 2, 2, 1]
        expected_count = 7
        solution = Solution()
        res = solution.candy(ratings)
        assert expected_count == res

    def test_case_four(self):
        ratings = [1, 2, 87, 87, 87, 2, 1]
        expected_count = 13
        solution = Solution()
        res = solution.candy(ratings)
        assert expected_count == res

    def test_case_five(self):
        ratings = [1, 6, 10, 8, 7, 3, 2]
        expected_count = 18
        solution = Solution()
        res = solution.candy(ratings)
        assert expected_count == res

    def test_case_six(self):
        ratings = [5, 4, 3, 2, 1]
        expected_count = 15
        solution = Solution()
        res = solution.candy(ratings)
        assert expected_count == res

    def test_case_seven(self):
        ratings = [1, 2, 3, 4, 5]
        expected_count = 15
        solution = Solution()
        res = solution.candy(ratings)
        assert expected_count == res

    def test_case_eight(self):
        ratings = [1, 3, 4, 5, 2]
        # [1,2,3,4,1]
        expected_count = 11 
        solution = Solution()
        res = solution.candy(ratings)
        assert expected_count == res
