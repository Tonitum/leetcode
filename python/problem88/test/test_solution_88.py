from problem88.python.solution import Solution


class TestSolution:

    def test_case_one(self):
        solution = Solution()
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        solution.merge(nums1, m, nums2, n)
        assert nums1 == [1,2,2,3,5,6]

    def test_case_two(self):
        solution = Solution()
        nums1 = [1]
        m = 1
        nums2: list[int] = []
        n = 0
        solution.merge(nums1, m, nums2, n)
        assert nums1 == [1]

    def test_case_three(self):
        solution = Solution()
        nums1 = [0]
        m = 0
        nums2: list[int] = [1]
        n = 1
        solution.merge(nums1, m, nums2, n)
        assert nums1 == [1]
