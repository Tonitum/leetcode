from python.neetcode_valid_anagram.solution import Solution


class TestSolution1004:
    def test_case_one(self):
        s = "racecar"
        t = "carrace"
        assert Solution().isAnagram(s,t)

    def test_case_two(self):
        s = "jar"
        t = "jam"
        assert not Solution().isAnagram(s,t)
