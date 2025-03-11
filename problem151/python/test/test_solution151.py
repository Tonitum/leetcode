from problem151.python.solution import Solution


class TestSolution151:
    def test_case_one(self):
        s = "the sky is blue"
        res = Solution().reverseWords(s)
        assert res == "blue is sky the"

    def test_case_two(self):
        s = "  hello world  "
        res = Solution().reverseWords(s)
        assert res == "world hello"

    def test_case_three(self):
        s = "a good   example"
        res = Solution().reverseWords(s)
        assert res == "example good a"
