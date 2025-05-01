from problem334.python.solution import Solution


class TestSolution334:
    def test_case_one(self):
        nums = [1, 2, 3, 4, 5]
        assert Solution().increasingTriplet(nums)

    def test_case_two(self):
        nums = [5, 4, 3, 2, 1]
        assert not Solution().increasingTriplet(nums)

    def test_case_three(self):
        nums = [2, 1, 5, 0, 4, 6]
        assert Solution().increasingTriplet(nums)

    def test_case_four(self):
        nums = [1, 5, 0, 4, 1, 3]
        assert Solution().increasingTriplet(nums)

    def test_case_five(self):
        nums = [20, 100, 10, 12, 5, 13]
        assert Solution().increasingTriplet(nums)

    def test_case_six(self):
        nums = [1, 0, 0, 0, 0, 0, 1, 100000000]
        assert Solution().increasingTriplet(nums)

    def test_case_seven(self):
        nums = [
            1,
            0,
            2,
            0,
            -1,
            -1,
            -1,
            -1,
            3,
        ]
        assert Solution().increasingTriplet(nums)
