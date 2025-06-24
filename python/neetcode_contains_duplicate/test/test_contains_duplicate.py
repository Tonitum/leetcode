from python.neetcode_contains_duplicate.solution import Solution


class TestSolution1004:
    def test_case_one(self):
        nums = [1,2,3,3]
        assert Solution().hasDuplicate(nums)

    def test_case_two(self):
        nums = [1,2,3,4]
        assert not Solution().hasDuplicate(nums)
