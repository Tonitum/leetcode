from problem80.python.solution import Solution


class TestSolution80:
    def test_case_one(self):
        solution = Solution()
        nums = [1,1,1,2,2,3]
        expected_output = [1,1,2,2,3]
        result = solution.removeDuplicates(nums)
        assert result == len(expected_output)
        nums[:] = nums[:result]
        for i in range(result):
            assert nums[i] == expected_output[i]

    def test_case_two(self):
        solution = Solution()
        nums = [0,0,1,1,1,1,2,3,3]
        expected_output = [0,0,1,1,2,3,3]
        result = solution.removeDuplicates(nums)
        assert result == len(expected_output)
        nums[:] = nums[:result]
        for i in range(result):
            assert nums[i] == expected_output[i]
