from problem1456.python.solution import Solution


class TestSolution1456:
    def test_case_one(self):
        s = "abciiidef"
        k = 3
        assert Solution().maxVowels(s, k) == 3

    def test_case_two(self):
        s = "aeiou"
        k = 2
        assert Solution().maxVowels(s, k) == 2

    def test_case_three(self):
        s = "tnfazcwrryitgacaabwm"
        k = 4
        assert Solution().maxVowels(s, k) == 3
        
    def test_case_four(self):
        s = "leetcode"
        k = 3
        assert Solution().maxVowels(s, k) == 2

    def test_case_five(self):
        s = "ramadan"
        k = 2
        assert Solution().maxVowels(s, k) == 1
