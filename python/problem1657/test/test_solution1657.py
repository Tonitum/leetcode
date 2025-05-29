from problem1657.python.solution import Solution


class TestSolution1657:
    def test_case_one(self):
        word1 = "abc"
        word2 = "bca"
        assert Solution().closeStrings(word1, word2)

    def test_case_two(self):
        word1 = "a"
        word2 = "aa"
        assert not Solution().closeStrings(word1, word2)

    def test_case_three(self):
        word1 = "cabbba"
        word2 = "abbccc"
        assert Solution().closeStrings(word1, word2)

    def test_case_four(self):
        word1 = "abbzzca"
        word2 = "babzzcz"
        assert not Solution().closeStrings(word1, word2)

    def test_case_five(self):
        word1 = "aaabbbbccddeeeeefffff"
        word2 = "aaaaabbcccdddeeeeffff"
        assert not Solution().closeStrings(word1, word2)
