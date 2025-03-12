class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_idx = 0
        found = False
        for i in range(len(s)):
            found = False
            curr = s[i]
            for j in range(t_idx, len(t)):
                if t[j] == curr:
                    found = True
                    t_idx = j + 1
                    break
            if not found:
                return False

        return True
        
