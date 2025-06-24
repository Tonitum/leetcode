class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Naive approach is to loop through the first string
        # for each char in the s string, iterate through the t string
        # if we find the char c in string t, remove it from string t and 
        # continue.
        # if we don't find char c in string t or t is of length 0, return false
        # once we loop all the way through, if length of string t is > 0 return false
        # otherwise, return true
        # space complexity is O(1)
        # time complexity is O(n^2)
        # for c in s:
        #     if len(t) == 0:
        #         return False
        #     match = t.find(c) # O(n)
        #     if match == -1:
        #         return False
        #     t = t[0:match] + t[match+1:]
        # if len(t) > 0:
        #     return False

        # return True
        # How else can we approach this, to be lower time complexity?
        # could create a map from s, with the key as the characters, and the value as the number of occurences
        # loop through t, and check map for char c. if char c exists, then subtract 1 from value.
        # if c is non present, or c's value is not > 0, return False, 
        # return true
        # time complexity is O(n+m)
        # space complexity is O(1)
        if len(s) != len(t):
            return False
        char_map: dict[str, int] = {}
        for sc in s:
            if sc not in char_map:
                char_map[sc] = 0
            char_map[sc] += 1

        for tc in t:
            if char_map.get(tc, 0) <= 0:
                return False
            char_map[tc] -= 1

        return True
