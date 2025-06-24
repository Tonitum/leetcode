class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        end = len(s) - 1

        while front < end:
            f_curr = s[front].lower()
            if not f_curr.isalnum():
                front = front + 1
                continue
            e_curr = s[end].lower()
            if not e_curr.isalnum():
                end = end - 1
                continue
            if f_curr != e_curr:
                return False
            front += 1
            end -= 1

        return True
