from python.neetcode_valid_palindrome.solution import Solution


class TestValidPalindrome:
    def test_case_one(self):
        s = "Was it a car or a cat I saw?"
        assert Solution().isPalindrome(s)

    def test_case_two(self):
        s = "tab a cat"
        assert not Solution().isPalindrome(s)
