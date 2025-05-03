from problem394.python.solution import Solution


class TestSolution394:
    def test_case_one(self):
        s = "3[a]2[bc]"
        assert Solution().decodeString(s) == "aaabcbc"

    def test_case_two(self):
        s = "3[a2[c]]"
        assert Solution().decodeString(s) == "accaccacc"

    def test_case_three(self):
        s = "2[abc]3[cd]ef"
        assert Solution().decodeString(s) == "abcabccdcdcdef"

    def test_case_four(self):
        s = "10[leetcode]"
        assert Solution().decodeString(s) == "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"
