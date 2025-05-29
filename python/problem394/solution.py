class Solution:
    def decodeString(self, s: str) -> str:
        # iterate forward until we find a number
        i = 0
        stack: list[str] = []
        while i < len(s):
            curr = s[i]
            if curr == "]":
                encoded_slice: str = ""
                k_parts: list[str] = []

                curr = stack.pop()
                while curr != "[":
                    encoded_slice = curr + encoded_slice
                    curr = stack.pop()

                while len(stack) > 0 and stack[len(stack)-1].isdigit():
                    curr = stack.pop()
                    k_parts.insert(0,curr)

                k = int("".join(k_parts))
                for _ in range(k):
                    for c in encoded_slice:
                        stack.append(c)
                i = i + 1
                continue

            stack.append(curr)
            i = i + 1
        return "".join(stack)
