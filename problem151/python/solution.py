class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words = ""
        temp_word = ""
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == " ":
                if temp_word != "":
                    reversed_words = reversed_words + temp_word + " "
                    temp_word = ""
                continue
            temp_word = c + temp_word
        if temp_word != "":
            reversed_words = reversed_words + temp_word
        return reversed_words.strip()
