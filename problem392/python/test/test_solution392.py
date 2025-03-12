from problem392.python.solution import Solution


class TestSolution392:
    def test_case_one(self):
        s = "abc"
        t = "ahbgdc"
        assert Solution().isSubsequence(s, t)
