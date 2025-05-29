from problem2215.python.solution import Solution


class TestSolution2215:
    def test_case_one(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]
        assert Solution().findDifference(nums1, nums2) == [[1, 3], [4, 6]]

    def test_case_two(self):
        nums1 = [1, 2, 3, 3]
        nums2 = [1, 1, 2, 2]
        assert Solution().findDifference(nums1, nums2) == [[3],[]]
