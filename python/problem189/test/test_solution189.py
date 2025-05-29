from problem189.python.solution import Solution

class TestSolution189:
    def test_case_one(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        expected_output = [5,6,7,1,2,3,4]
        solution = Solution()
        solution.rotate(nums, k)
        assert nums == expected_output

    def test_case_two(self):
        nums = [-1,-100,3,99]
        k = 2 
        expected_output = [3,99,-1,-100]
        solution = Solution()
        solution.rotate(nums, k)
        assert nums == expected_output

    def test_case_three(self):
        nums = [1,2]
        k = 5 
        expected_output = [2,1]
        solution = Solution()
        solution.rotate(nums, k)
        assert nums == expected_output

    def test_case_one1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        expected_output = [5,6,7,1,2,3,4]
        solution = Solution()
        solution.rotate1(nums, k)
        assert nums == expected_output

    def test_case_two1(self):
        nums = [-1,-100,3,99]
        k = 2 
        expected_output = [3,99,-1,-100]
        solution = Solution()
        solution.rotate1(nums, k)
        assert nums == expected_output

    def test_case_three1(self):
        nums = [1,2]
        k = 5 
        expected_output = [2,1]
        solution = Solution()
        solution.rotate1(nums, k)
        assert nums == expected_output
