class Solution:
    def compress(self, chars: list[str]) -> int:
        compressed = ""
        temp_count = 1
        curr = chars[0]
        for c in chars[1:]:
            if c == curr:
                temp_count = temp_count + 1
                continue
            compressed = (
                compressed + curr + str(temp_count)
                if temp_count > 1
                else compressed + curr
            )
            curr = c
            temp_count = 1
            continue

        if temp_count > 0:
            compressed = (
                compressed + curr + str(temp_count)
                if temp_count > 1
                else compressed + curr
            )

        chars[:] = list(compressed)
        return len(compressed)
