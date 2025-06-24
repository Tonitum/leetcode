from python.neetcode_valid_paren.solution import Solution


class TestValidParen:
    def test_case_one(self):
        s = "[]"
        assert Solution().isValid(s)

    def test_case_two(self):
        s = "([{}])"
        assert Solution().isValid(s)

    def test_case_three(self):
        s = "[(])"
        assert not Solution().isValid(s)
