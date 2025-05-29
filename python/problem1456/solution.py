class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        vowel_count_in_substring = 0
        vowels = {"a", "e", "i", "o", "u"}
        for i in range(k):
            if s[i] in vowels:
                vowel_count_in_substring = vowel_count_in_substring + 1

        max_count = vowel_count_in_substring
        for i in range(k, len(s)):
            c = s[i]
            if c in vowels:
                if vowel_count_in_substring < k:
                    vowel_count_in_substring = vowel_count_in_substring + 1
            if s[i-k] in vowels:
                vowel_count_in_substring = vowel_count_in_substring - 1
            if vowel_count_in_substring > max_count:
                max_count = vowel_count_in_substring
        return max_count
