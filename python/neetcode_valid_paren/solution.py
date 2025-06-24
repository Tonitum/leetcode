class Solution:
    def isValid(self, s: str) -> bool:
        brackets: list[str] = []
        PAIRS = {"[": "]", "{": "}", "(": ")"}
        for c in s:
            if c in PAIRS:
                brackets.append(c)
                continue
            if not len(brackets) > 0:
                return False
            if c in PAIRS.values():
                match = brackets.pop()
                if PAIRS[match] != c:
                    return False
        if len(brackets) > 0:
            return False
        return True

