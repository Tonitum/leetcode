from problem26.python.solution import Solution


class TestSolution26:
    def test_case_one(self):
        solution = Solution()
        nums = [1,1,2]
        expected_output = [1,2]
        result = solution.removeDuplicates(nums)
        assert result == len(expected_output)
        nums[:] = nums[:result]
        for i in range(result):
            assert nums[i] == expected_output[i]

    def test_case_two(self):
        solution = Solution()
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected_output = [0,1,2,3,4]
        result = solution.removeDuplicates(nums)
        assert result == len(expected_output)
        nums[:] = nums[:result]
        for i in range(result):
            assert nums[i] == expected_output[i]

    def test_case_three(self):
        solution = Solution()
        nums = [1]
        expected_output = [1]
        result = solution.removeDuplicates(nums)
        assert result == len(expected_output)
        nums[:] = nums[:result]
        for i in range(result):
            assert nums[i] == expected_output[i]
