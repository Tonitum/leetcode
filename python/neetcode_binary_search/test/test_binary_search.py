from python.neetcode_binary_search.solution import Solution


class TestBinarySearch:
    def test_case_one(self):
        nums = [-1,0,2,4,6,8]
        target = 4
        assert Solution().search(nums, target) == 3

    def test_case_two(self):
        nums = [-1,0,2,4,6,8]
        target = 3
        assert Solution().search(nums, target) == -1
