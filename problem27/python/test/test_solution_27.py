from problem27.python.solution import Solution


class TestSolution27:
    def test_case_one(self):
        solution = Solution()
        nums = [3, 2, 2, 3]
        expected_nums = [2, 2]
        val = 3
        val_count = solution.removeElement(nums, val)
        assert val_count == len(expected_nums)
        nums[:] = nums[:val_count]
        nums.sort()
        for i in range(len(expected_nums)):
            assert nums[i] == expected_nums[i]

    def test_case_two(self):
        solution = Solution()
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        expected_nums = [0, 0, 1, 3, 4]
        val = 2
        val_count = solution.removeElement(nums, val)
        assert val_count == len(expected_nums)
        nums[:] = nums[:val_count]
        nums.sort()
        for i in range(len(expected_nums)):
            assert nums[i] == expected_nums[i]
